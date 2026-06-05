-- Tutorial 4 starter: application query side for climate_station.db.
-- Complete these SQL statements first, then translate them into Python functions.

-- Question 1:
-- What are the most recent readings?
SELECT
    -- TODO: reading id
    -- TODO: location name
    -- TODO: device name
    -- TODO: measured_at
    -- TODO: temperature, humidity, pressure
FROM SensorReading sr
-- TODO: join Device
-- TODO: join Location
ORDER BY
    -- TODO: newest first
LIMIT ?;

-- Question 2:
-- What is the daily climate summary per location?
SELECT
    -- TODO: reading date
    -- TODO: location name
    -- TODO: avg/min/max temperature
    -- TODO: avg humidity
    -- TODO: avg pressure
FROM SensorReading sr
-- TODO: join Device
-- TODO: join Location
GROUP BY
    -- TODO: date and location
ORDER BY
    -- TODO: newest date first
;

-- Question 3:
-- Which readings are outside their comfort profile?
SELECT
    -- TODO: location name
    -- TODO: measured_at
    -- TODO: temperature, humidity
    -- TODO: readable status with CASE
FROM SensorReading sr
-- TODO: join Device, Location, ComfortProfile
WHERE
    -- TODO: temperature or humidity outside configured range
ORDER BY
    -- TODO: newest first
;

-- Question 4:
-- Which devices are installed in a location?
SELECT
    -- TODO: device fields
FROM Device
WHERE location_id = ?
ORDER BY
    -- TODO
;

-- Question 5:
-- Insert a manual test reading.
INSERT INTO SensorReading (
    device_id,
    measured_at,
    temperature_c,
    humidity_percent,
    pressure_hpa
)
VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?);
