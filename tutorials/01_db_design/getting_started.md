# Tutorial 1: Design the Climate Station Database

**Tool:** ChartDB with Docker Desktop

**Goal:** Use ChartDB to design the SQLite database that will store ESP32/BME280 climate measurements in the next tutorial.

## Step 1: Install and Start ChartDB

ChartDB runs locally in Docker Desktop. If Docker is not installed yet, complete `../00_windows_setup/getting_started.md` first.

Start ChartDB:

```bash
docker run -d -p 8080:80 ghcr.io/chartdb/chartdb:latest
```

Open:

```text
http://localhost:8080
```

If the port is already in use, stop the old container or run ChartDB on another port, for example `-p 8081:80`.

## Step 2: Create the Climate Station Diagram

1. Use `climate_station_starter.dbml` as a design checklist, not as a finished answer.
2. In ChartDB, create the missing tables, attributes, primary keys, and foreign keys.
3. Export your final design as SQL if ChartDB provides SQL export in your version.
4. If you export DBML instead, use the optional DBML conversion step below.

## Step 3: Check the Model

For each diagram, answer:

1. What are the entities?
2. What is the primary key of each entity?
3. Which tables contain foreign keys?
4. Which relationship is one-to-many?
5. Which relationship is many-to-many, and which junction table resolves it?

## Step 4: Optional DBML to SQLite SQL Conversion

If your ChartDB workflow exports DBML instead of SQL, install the converter:

```bash
python -m pip install dbml-sqlite
```

The package installs a command named `dbml_sqlite`.

Convert your exported or completed DBML to a `.sql` file:

```bash
dbml_sqlite --no-print --write climate_station_generated.sql --if-table-exists climate_station_starter.dbml
```

You can also execute the generated DDL directly into a SQLite database:

```bash
dbml_sqlite --no-print --write climate_station_generated.sql --execute climate_station.db --if-table-exists climate_station_starter.dbml
```

Open `climate_station_generated.sql` and inspect it before loading it in DB Browser for SQLite.

## Step 5: Load the SQL in DB Browser

1. Open DB Browser for SQLite.
2. Create a new database named `climate_station.db`.
3. Open the SQL execution tab.
4. Run your ChartDB-exported SQL or your generated `climate_station_generated.sql`.
5. Confirm that your tables and foreign keys were created.

## Deliverables

- Screenshot or export of the climate station ER diagram
- Final ChartDB diagram export
- SQL DDL exported from ChartDB or generated from DBML
- Short explanation of 1NF, 2NF, and 3NF in your climate station design
