# ESP32 BME280 Climate Station with SQLite

This repository contains an ESP32-based climate data project. An ESP32 reads a BME280 sensor, sends temperature, humidity, and pressure values over WiFi, and a Python host receiver stores the readings in SQLite.

The database tutorials now build one continuous project around this system:

1. Design the climate database in ChartDB.
2. Send ESP32/BME280 data into SQLite.
3. Analyze the climate readings with SQL.
4. Build a small Python application on top of the same database.

The project can be used as a small weather station or as a smart-home indoor climate monitor.

## Requirements

- ESP32 microcontroller
- BME280 sensor with I2C wiring
- Thonny IDE
- Python 3.10+ on the host computer
- DB Browser for SQLite: https://sqlitebrowser.org/
- Docker Desktop for running ChartDB locally
- Optional WSL 2 on Windows for a smoother Docker workflow

SQLite itself is included with Python through the built-in `sqlite3` module. The only optional Python package used by the tutorials is:

```text
dbml-sqlite
```

## ESP32 Setup

Open the files in `esp32-code/`.

1. Edit `esp32-code/secure.txt` with your WiFi credentials.
2. Open `esp32-code/main.py`.
3. Set `server_ip` to your computer's IPv4 address.
4. Check the BME280 I2C pins:

```python
sda_pin = 19
scl_pin = 18
```

5. In Thonny, copy these files to the ESP32:

- `boot.py`
- `main.py`
- `bme280.py`
- `secure.txt`

When `main.py` runs, it sends messages like:

```text
Temperature: 22.4, Humidity: 45.2, Pressure: 1013.6
```

## Host Receiver

Run the host receiver on your computer:

```bash
python LeesESP32_SQlite.py
```

The receiver:

- listens on `0.0.0.0:5000`
- creates or opens `climate_station.db`
- creates default `Location`, `Device`, and `SensorReading` tables if needed
- stores each ESP32/BME280 reading in SQLite

Open `climate_station.db` in DB Browser for SQLite to inspect the readings.

## ChartDB for Tutorial 1

Tutorial 1 uses ChartDB for schema design.

Install/start ChartDB with Docker Desktop:

```bash
docker run -d -p 8080:80 ghcr.io/chartdb/chartdb:latest
```

Open:

```text
http://localhost:8080
```

If students export DBML from ChartDB, convert it to SQLite SQL with:

```bash
python -m pip install dbml-sqlite
dbml_sqlite --no-print --write climate_station_generated.sql --if-table-exists tutorials/01_db_design/climate_station_starter.dbml
```

## Tutorial Starter Kit

Start here:

| Tutorial | Starter |
|---|---|
| ChartDB and Docker setup | `tutorials/00_windows_setup/getting_started.md` |
| 1. Design the climate database | `tutorials/01_db_design/getting_started.md` |
| 2. Capture ESP32 BME280 data | `tutorials/02_sql_real_work/getting_started.md` |
| 3. Analyze climate data | `tutorials/03_climate_analysis/getting_started.md` |
| 4. Build a SQLite climate app | `tutorials/04_sqlite_application/getting_started.md` |

The course reader is:

```text
Course-reader-lab-manual.md
```

## File Overview

| Path | Description |
|---|---|
| `esp32-code/boot.py` | Connects ESP32 to WiFi |
| `esp32-code/main.py` | Reads BME280 and sends data to the host |
| `esp32-code/bme280.py` | BME280 MicroPython driver |
| `esp32-code/secure.txt` | WiFi credentials |
| `LeesESP32_SQlite.py` | Host-side receiver and SQLite writer |
| `tutorials/` | Lab starter files |
| `requirements.txt` | Optional Python dependencies |

## Notes

- The ESP32 and host computer must be on the same WiFi network.
- Many WiFi issues come from using a 5 GHz-only network; ESP32 boards often need 2.4 GHz.
- The receiver stores plain sensor values for teaching purposes.
- For production systems, add authentication, input validation, and more robust error handling.
