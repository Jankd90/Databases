# Tutorial 2: Capture ESP32 BME280 Data in SQLite

**Tools:** ESP32, BME280, Thonny, Python, DB Browser for SQLite

**Goal:** Send real temperature, humidity, and pressure readings from the ESP32 to the `climate_station.db` database designed in Tutorial 1.

## Step 1: Prepare the Database From Tutorial 1

1. Open DB Browser for SQLite.
2. Open the `climate_station.db` database from Tutorial 1.
3. Run your generated SQL file from Tutorial 1, for example `../01_db_design/climate_station_generated.sql`.
4. Insert at least one `Location`, one `Device`, and one `ComfortProfile`.

If you do not have hardware available during class, copy `sample_data_starter.sql` to your own work file and insert realistic sample readings.

## Step 2: Configure the ESP32

1. Open `esp32-code/main.py` in Thonny.
2. Set `server_ip` to your computer's IPv4 address.
3. Confirm the BME280 I2C pins match your wiring.
4. Copy `boot.py`, `main.py`, `bme280.py`, and `secure.txt` to the ESP32.

The ESP32 sends data in this shape:

```text
Temperature: 22.4, Humidity: 45.2, Pressure: 1013.6
```

## Step 3: Run the Host Receiver

Run the Python receiver on your computer:

```bash
python LeesESP32_SQlite.py
```

The receiver listens on port `5000`, parses incoming BME280 values, and inserts them into SQLite.

## Step 4: Run Reporting Queries

1. Open `reporting_queries_starter.sql`.
2. Execute one query at a time.
3. Fill in the TODO sections until each result answers the climate question above it.

## Step 5: Add Views and Indexes

Copy `views_and_indexes_starter.sql` to your own work file, then complete and run it.

Then test:

```sql
SELECT *
FROM DailyClimateSummary;
```

## Deliverables

- Working ESP32-to-SQLite capture, or completed fallback sample data script
- Completed reporting query script
- `DailyClimateSummary` view
- At least three indexes
- Short explanation of how one `JOIN`, one `GROUP BY`, one view, and one index help the weather station or smart-home climate project
