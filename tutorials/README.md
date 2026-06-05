# Climate Station Tutorial Starter Kit

This folder contains starter files for the four SQLite tutorials in `Course-reader-lab-manual.md`.

The tutorials build one continuous project: an ESP32/BME280 weather station or smart-home indoor climate monitor.

## Folder Overview

| Folder | Purpose |
|---|---|
| `00_windows_setup` | Install Docker Desktop for running ChartDB locally |
| `01_db_design` | Design the climate station schema in ChartDB, then create tables in SQLite |
| `02_sql_real_work` | Capture ESP32/BME280 readings and run reporting SQL |
| `03_climate_analysis` | Analyze climate readings with advanced SQL and location hierarchies |
| `04_sqlite_application` | Build a small Python application backed by the climate SQLite database |

## Suggested Student Workflow

1. Windows students start with `00_windows_setup/getting_started.md`.
2. Continue with `01_db_design/getting_started.md`.
3. Start ChartDB with `docker run -d -p 8080:80 ghcr.io/chartdb/chartdb:latest`.
4. Complete the climate station schema model in ChartDB.
5. Export SQL from ChartDB, or export DBML and convert it with `dbml_sqlite`.
6. Load the generated `.sql` file into `climate_station.db` with DB Browser for SQLite.
7. Run `LeesESP32_SQlite.py` and send BME280 readings from the ESP32.
8. Complete the SQL starter files for reporting, climate analysis, and application workflows.
9. Use `04_sqlite_application/app_starter.py` after running its migration and seed commands.

## Optional DBML to SQLite Conversion

If ChartDB exports SQL directly, use that SQL. If you export DBML, install the converter:

```bash
python -m pip install dbml-sqlite
```

Convert DBML to a SQL file:

```bash
dbml_sqlite --no-print --write climate_station_generated.sql --if-table-exists tutorials/01_db_design/climate_station_starter.dbml
```

The provided tutorial files are not answer keys. They are intentionally small starters so students must design the schema, capture or simulate sensor data, write the SQL, and complete the application behavior themselves.
