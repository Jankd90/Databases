# Course Reader & Laboratory Manual

**Title:** Applied SQLite: ESP32 Weather Station and Smart-Home Climate Data

**Estimated Time:** 4 Tutorials x 2 Hours (8 Hours Total)

**Tools:** ChartDB, DB Browser for SQLite, SQLite, Python, Thonny, ESP32, BME280, Docker Desktop

## Course Overview

This course is one continuous project. Students design, build, populate, analyze, and use a SQLite database for climate measurements from an ESP32 with a BME280 sensor.

The project can be framed in two ways:

- **Weather station:** an indoor/outdoor measurement system for temperature, humidity, and pressure.
- **Smart-home indoor climate:** a room-monitoring system that checks comfort ranges and generates alerts.

By the end of the course, students will have:

- a ChartDB ER diagram
- SQLite DDL
- a working `climate_station.db`
- ESP32/BME280 readings stored in SQLite
- SQL reports, views, and indexes
- climate analysis queries
- a small Python application that reads the same database

## Tutorial Roadmap

| Tutorial | Main Tool | Main Skill | Main Output |
|---|---|---|---|
| 1. Design the Climate Database | ChartDB and DB Browser for SQLite | Data modeling | ER diagram and SQLite schema |
| 2. Capture ESP32 Data | ESP32, BME280, Python, SQLite | Device-to-database pipeline | Real readings in `climate_station.db` |
| 3. Analyze Climate Data | SQLite and DB Browser | Analytical SQL | summaries, alerts, recursive/location queries |
| 4. Build a Climate App | Python and SQLite | Application database access | CLI app with parameters and transactions |

## Core Project Schema

The exact design can vary, but the course assumes these core entities:

- `Location`: room, balcony, lab, greenhouse, or outdoor station position
- `Device`: ESP32/BME280 unit installed at a location
- `SensorReading`: timestamped temperature, humidity, and pressure values
- `ComfortProfile`: acceptable temperature and humidity ranges per location
- `ClimateAlert` or `AlertEvent`: readings that violate comfort or safety rules

Minimum reading columns:

```sql
temperature_c REAL NOT NULL,
humidity_percent REAL NOT NULL,
pressure_hpa REAL NOT NULL,
measured_at TEXT NOT NULL
```

## Tutorial 1: Design the Climate Station Database

**Tools:** ChartDB, Docker Desktop, DB Browser for SQLite

**Core Emphasis:** Designing before collecting data

### Learning Goal

Students use ChartDB to design the database that will receive real BME280 readings in Tutorial 2.

### Small ChartDB Installation Guide

1. Install Docker Desktop.
2. Start Docker Desktop.
3. Open PowerShell or a terminal.
4. Run:

```bash
docker run -d -p 8080:80 ghcr.io/chartdb/chartdb:latest
```

5. Open:

```text
http://localhost:8080
```

If `8080` is already in use, run ChartDB on another port:

```bash
docker run -d -p 8081:80 ghcr.io/chartdb/chartdb:latest
```

Then open `http://localhost:8081`.

### Starter Files

Use:

- `tutorials/01_db_design/getting_started.md`
- `tutorials/01_db_design/climate_station_starter.dbml`

Students complete the model in ChartDB, then export SQL. If ChartDB exports DBML instead of SQLite SQL, convert it:

```bash
python -m pip install dbml-sqlite
dbml_sqlite --no-print --write climate_station_generated.sql --if-table-exists tutorials/01_db_design/climate_station_starter.dbml
```

Create or open `climate_station.db` in DB Browser for SQLite and run the generated SQL.

### Required Design Questions

1. Which table stores rooms or outdoor sensor positions?
2. Which table stores the ESP32/BME280 device?
3. Which table stores each timestamped measurement?
4. Why should location details not be repeated on every reading row?
5. How does the design support more than one sensor?
6. How can the same schema support both a weather station and a smart-home indoor climate system?

### Tutorial 1 Deliverables

- ChartDB ER diagram
- `climate_station_generated.sql` or equivalent exported DDL
- working `climate_station.db`
- short explanation of primary keys, foreign keys, and normalization

## Tutorial 2: Capture ESP32 BME280 Data in SQLite

**Tools:** ESP32, BME280, Thonny, Python, SQLite

**Core Emphasis:** Moving real device data into a database

### Learning Goal

Students connect the ESP32/BME280 to the host computer and store real sensor readings in the database designed in Tutorial 1.

### Hardware and Code Setup

Use the files in `esp32-code/`:

- `boot.py`
- `main.py`
- `bme280.py`
- `secure.txt`

In `esp32-code/main.py`, set:

```python
server_ip = "YOUR_COMPUTER_IPV4_ADDRESS"
server_port = 5000
```

The ESP32 sends messages like:

```text
Temperature: 22.4, Humidity: 45.2, Pressure: 1013.6
```

### Host Receiver

Run the host receiver:

```bash
python LeesESP32_SQlite.py
```

The receiver:

- listens on `0.0.0.0:5000`
- parses temperature, humidity, and pressure
- creates default `Location`, `Device`, and `SensorReading` tables if needed
- inserts each reading into `climate_station.db`

### Fallback Data

If hardware is unavailable, use:

- `tutorials/02_sql_real_work/sample_data_starter.sql`

The fallback data should still match the same climate schema so later tutorials work.

### SQL Work

Use:

- `tutorials/02_sql_real_work/reporting_queries_starter.sql`
- `tutorials/02_sql_real_work/views_and_indexes_starter.sql`

Students write queries for:

- latest reading per device
- average temperature per day
- highest humidity readings
- readings outside comfort profiles
- readings per device per hour
- pressure trend using `LAG`

### Tutorial 2 Deliverables

- ESP32 readings stored in `climate_station.db`, or realistic fallback readings
- completed climate reporting queries
- `DailyClimateSummary` view
- indexes for timestamp, device, and location lookups
- short explanation of the data pipeline from sensor to SQLite

## Tutorial 3: Analyze Climate Data

**Tools:** SQLite and DB Browser for SQLite

**Core Emphasis:** Turning raw readings into useful climate insight

### Learning Goal

Students use the readings from Tutorial 2 to answer weather-station or smart-home climate questions.

### Starter Files

Use:

- `tutorials/03_climate_analysis/getting_started.md`
- `tutorials/03_climate_analysis/analysis_schema_starter.sql`
- `tutorials/03_climate_analysis/recursive_queries_starter.sql`
- `tutorials/03_climate_analysis/climate_analysis_queries_starter.sql`

### Analysis Tasks

Students add analysis structures such as:

- `LocationHierarchy`: building, floor, room, outdoor zone
- `AlertRule`: thresholds for temperature, humidity, or pressure
- `AlertEvent`: readings that violated a rule

Students write SQL for:

- all rooms under a building or floor using `WITH RECURSIVE`
- all readings under a chosen parent location
- alert counts by location and severity
- daily indoor climate summaries
- pressure trend
- rooms with similar climate behavior

### Tutorial 3 Deliverables

- completed analysis schema
- at least one location hierarchy
- at least three recursive CTE queries
- at least four climate analysis queries
- short interpretation of what the measurements say

## Tutorial 4: Build a SQLite Climate Application

**Tools:** Python and SQLite

**Core Emphasis:** Using the database from application code

### Learning Goal

Students build a small command-line application that reads and writes the same climate database used in the earlier tutorials.

### Starter Files

Use:

- `tutorials/04_sqlite_application/getting_started.md`
- `tutorials/04_sqlite_application/app_starter.py`
- `tutorials/04_sqlite_application/application_queries_starter.sql`
- `tutorials/04_sqlite_application/migrations/001_create_schema.sql`
- `tutorials/04_sqlite_application/seed_data.sql`

Example commands:

```bash
python app_starter.py migrate --database climate_station_app.db
python app_starter.py seed --database climate_station_app.db
python app_starter.py readings --database climate_station_app.db
python app_starter.py summary --database climate_station_app.db
python app_starter.py alerts --database climate_station_app.db
```

### Application Requirements

The app should support:

- adding a location
- adding a device
- adding a manual reading for testing
- listing recent readings
- showing daily summaries
- listing comfort alerts

Students must use parameterized queries and at least one transaction.

### Tutorial 4 Deliverables

- working climate CLI application
- at least four parameterized queries
- at least one transaction
- short explanation of how the app uses the ESP32/BME280 data

## Final Portfolio

| Artifact | Source Tutorial | Description |
|---|---|---|
| ER diagram | Tutorial 1 | climate station schema in ChartDB |
| SQLite DDL | Tutorial 1 | `CREATE TABLE` statements |
| Sensor data | Tutorial 2 | real or fallback BME280 readings |
| SQL reports | Tutorial 2 | reporting queries, view, and indexes |
| Climate analysis | Tutorial 3 | recursive and analytical SQL |
| Python app | Tutorial 4 | SQLite application code |

## Assessment Rubric

| Category | Weight | Criteria |
|---|---:|---|
| Data Modeling | 25% | Schema separates locations, devices, readings, profiles, and alerts clearly. |
| Sensor Data Pipeline | 25% | ESP32/BME280 data is captured or realistically simulated and stored correctly. |
| SQL Analysis | 25% | Queries use joins, grouping, views, indexes, recursive CTEs, and trend analysis appropriately. |
| SQLite Application | 25% | Application code uses parameterized queries, transactions, and useful climate commands. |

## Final Reflection Questions

1. How does your schema support both a weather station and a smart-home indoor climate use case?
2. What data quality problems could happen when receiving sensor readings over WiFi?
3. Which SQL query gave the most useful climate insight?
4. Why are timestamp and device indexes important for this project?
5. How would you extend the system with another sensor or another room?
