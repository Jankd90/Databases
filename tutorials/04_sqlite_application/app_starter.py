"""Tutorial 4 starter: a small SQLite-backed climate application.

Example commands:

python app_starter.py migrate --database climate_station_app.db
python app_starter.py seed --database climate_station_app.db
python app_starter.py readings --database climate_station_app.db
python app_starter.py summary --database climate_station_app.db
python app_starter.py alerts --database climate_station_app.db
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MIGRATION_FILE = BASE_DIR / "migrations" / "001_create_schema.sql"
SEED_FILE = BASE_DIR / "seed_data.sql"


def connect(database: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def run_script(database: Path, script_path: Path) -> None:
    with connect(database) as conn:
        conn.executescript(script_path.read_text(encoding="utf-8"))


def add_location(database: Path, name: str, location_type: str, floor: str | None) -> None:
    with connect(database) as conn:
        # TODO: use a parameterized INSERT statement.
        raise NotImplementedError("Complete add_location()")


def add_device(database: Path, device_name: str, location_id: int) -> None:
    with connect(database) as conn:
        # TODO: use a parameterized INSERT statement.
        raise NotImplementedError("Complete add_device()")


def add_reading(
    database: Path,
    device_id: int,
    temperature_c: float,
    humidity_percent: float,
    pressure_hpa: float,
) -> None:
    with connect(database) as conn:
        # TODO: use a parameterized INSERT statement.
        raise NotImplementedError("Complete add_reading()")


def add_device_with_first_reading(
    database: Path,
    device_name: str,
    location_id: int,
    temperature_c: float,
    humidity_percent: float,
    pressure_hpa: float,
) -> None:
    with connect(database) as conn:
        try:
            conn.execute("BEGIN")
            # TODO: insert the Device row.
            # TODO: use cursor.lastrowid as the device_id for the first SensorReading.
            # TODO: insert the first SensorReading row.
            conn.commit()
        except sqlite3.Error:
            conn.rollback()
            raise


def recent_readings(database: Path, limit: int) -> None:
    with connect(database) as conn:
        rows = conn.execute(
            """
            SELECT
                sr.reading_id,
                l.name AS location_name,
                d.device_name,
                sr.measured_at,
                sr.temperature_c,
                sr.humidity_percent,
                sr.pressure_hpa
            FROM SensorReading sr
            JOIN Device d ON d.device_id = sr.device_id
            JOIN Location l ON l.location_id = d.location_id
            ORDER BY sr.measured_at DESC, sr.reading_id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    for row in rows:
        print(
            f"{row['measured_at']} | {row['location_name']:<14} | "
            f"{row['temperature_c']:>5.1f} C | {row['humidity_percent']:>5.1f}% | "
            f"{row['pressure_hpa']:>7.1f} hPa"
        )


def daily_summary(database: Path) -> None:
    with connect(database) as conn:
        rows = conn.execute(
            """
            SELECT
                date(sr.measured_at) AS reading_date,
                l.name AS location_name,
                COUNT(*) AS reading_count,
                AVG(sr.temperature_c) AS avg_temperature_c,
                AVG(sr.humidity_percent) AS avg_humidity_percent,
                AVG(sr.pressure_hpa) AS avg_pressure_hpa
            FROM SensorReading sr
            JOIN Device d ON d.device_id = sr.device_id
            JOIN Location l ON l.location_id = d.location_id
            GROUP BY date(sr.measured_at), l.location_id, l.name
            ORDER BY reading_date DESC, l.name
            """
        ).fetchall()

    for row in rows:
        print(
            f"{row['reading_date']} | {row['location_name']:<14} | "
            f"{row['reading_count']:>3} readings | "
            f"{row['avg_temperature_c']:>5.1f} C | "
            f"{row['avg_humidity_percent']:>5.1f}% | "
            f"{row['avg_pressure_hpa']:>7.1f} hPa"
        )


def comfort_alerts(database: Path) -> None:
    with connect(database) as conn:
        rows = conn.execute(
            """
            SELECT
                l.name AS location_name,
                sr.measured_at,
                sr.temperature_c,
                sr.humidity_percent,
                CASE
                    WHEN sr.temperature_c < cp.min_temperature_c THEN 'too cold'
                    WHEN sr.temperature_c > cp.max_temperature_c THEN 'too hot'
                    WHEN sr.humidity_percent < cp.min_humidity_percent THEN 'too dry'
                    WHEN sr.humidity_percent > cp.max_humidity_percent THEN 'too humid'
                    ELSE 'ok'
                END AS alert_status
            FROM SensorReading sr
            JOIN Device d ON d.device_id = sr.device_id
            JOIN Location l ON l.location_id = d.location_id
            JOIN ComfortProfile cp ON cp.location_id = l.location_id
            WHERE
                sr.temperature_c < cp.min_temperature_c
                OR sr.temperature_c > cp.max_temperature_c
                OR sr.humidity_percent < cp.min_humidity_percent
                OR sr.humidity_percent > cp.max_humidity_percent
            ORDER BY sr.measured_at DESC
            """
        ).fetchall()

    for row in rows:
        print(
            f"{row['measured_at']} | {row['location_name']:<14} | "
            f"{row['alert_status']:<9} | {row['temperature_c']:>5.1f} C | "
            f"{row['humidity_percent']:>5.1f}%"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tutorial 4 SQLite climate application starter.")
    database_parent = argparse.ArgumentParser(add_help=False)
    database_parent.add_argument("--database", type=Path, default=Path("climate_station.db"))
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("migrate", parents=[database_parent])
    subparsers.add_parser("seed", parents=[database_parent])

    readings_parser = subparsers.add_parser("readings", parents=[database_parent])
    readings_parser.add_argument("--limit", type=int, default=10)

    subparsers.add_parser("summary", parents=[database_parent])
    subparsers.add_parser("alerts", parents=[database_parent])

    location_parser = subparsers.add_parser("add-location", parents=[database_parent])
    location_parser.add_argument("name")
    location_parser.add_argument("location_type")
    location_parser.add_argument("--floor")

    device_parser = subparsers.add_parser("add-device", parents=[database_parent])
    device_parser.add_argument("device_name")
    device_parser.add_argument("location_id", type=int)

    reading_parser = subparsers.add_parser("add-reading", parents=[database_parent])
    reading_parser.add_argument("device_id", type=int)
    reading_parser.add_argument("temperature_c", type=float)
    reading_parser.add_argument("humidity_percent", type=float)
    reading_parser.add_argument("pressure_hpa", type=float)

    first_parser = subparsers.add_parser("add-device-with-reading", parents=[database_parent])
    first_parser.add_argument("device_name")
    first_parser.add_argument("location_id", type=int)
    first_parser.add_argument("temperature_c", type=float)
    first_parser.add_argument("humidity_percent", type=float)
    first_parser.add_argument("pressure_hpa", type=float)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    database = args.database.resolve()

    if args.command == "migrate":
        run_script(database, MIGRATION_FILE)
    elif args.command == "seed":
        run_script(database, SEED_FILE)
    elif args.command == "readings":
        recent_readings(database, args.limit)
    elif args.command == "summary":
        daily_summary(database)
    elif args.command == "alerts":
        comfort_alerts(database)
    elif args.command == "add-location":
        add_location(database, args.name, args.location_type, args.floor)
    elif args.command == "add-device":
        add_device(database, args.device_name, args.location_id)
    elif args.command == "add-reading":
        add_reading(
            database,
            args.device_id,
            args.temperature_c,
            args.humidity_percent,
            args.pressure_hpa,
        )
    elif args.command == "add-device-with-reading":
        add_device_with_first_reading(
            database,
            args.device_name,
            args.location_id,
            args.temperature_c,
            args.humidity_percent,
            args.pressure_hpa,
        )


if __name__ == "__main__":
    main()
