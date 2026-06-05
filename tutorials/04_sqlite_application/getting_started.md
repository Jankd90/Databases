# Tutorial 4: Build a SQLite Climate Application

**Tools:** Python, SQLite, DB Browser for SQLite

**Goal:** Build a small command-line application around the climate station database created in Tutorials 1-3.

## Step 1: Continue With the Same Project Database

Use `climate_station.db` from Tutorial 2. If you need a clean practice database, run:

```bash
python app_starter.py migrate --database climate_station_app.db
python app_starter.py seed --database climate_station_app.db
```

## Step 2: Inspect Climate Data

Run:

```bash
python app_starter.py readings --database climate_station.db
python app_starter.py summary --database climate_station.db
python app_starter.py alerts --database climate_station.db
```

These commands should read the same `SensorReading` rows created by the ESP32 receiver in Tutorial 2.

## Step 3: Complete Application Commands

Open `app_starter.py` and complete the TODO sections.

Your app should support:

1. Adding a new location.
2. Adding a new device assigned to a location.
3. Adding a manual reading for testing.
4. Showing recent readings.
5. Showing daily summaries.
6. Listing readings outside comfort profiles.

## Step 4: Use Parameterized Queries

Open `application_queries_starter.sql` and translate the important queries into Python functions.

Do not build SQL by joining user input into strings. Use SQLite parameters such as:

```python
cursor.execute(
    "SELECT * FROM SensorReading WHERE measured_at >= ?",
    (start_time,),
)
```

## Step 5: Use Transactions

Adding a device and its first test reading should be one transaction:

1. Insert the device.
2. Insert the first reading.
3. Commit only when both rows succeed.
4. Roll back if one row fails.

## Deliverables

- Working climate application database
- Completed Python commands
- At least one transaction
- At least four parameterized queries
- Short explanation of how the app uses the ESP32/BME280 data collected earlier
