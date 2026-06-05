-- Tutorial 2 climate reporting query starters.
-- Replace TODO sections with your own SQL.
-- Adjust table and column names if your ChartDB design uses different names.

-- 1. Latest reading per device.
-- Required concepts: JOIN, subquery or MAX.
SELECT
    -- TODO: device name
    -- TODO: location name
    -- TODO: measured_at
    -- TODO: temperature, humidity, pressure
FROM SensorReading sr
-- TODO: join Device
-- TODO: join Location
WHERE
    -- TODO: keep only the newest reading for each device
;

-- 2. Average indoor temperature per day.
-- Required concepts: JOIN, date(), AVG, GROUP BY.
SELECT
    -- TODO
FROM SensorReading sr
-- TODO
GROUP BY
    -- TODO: date and location
;

-- 3. Highest humidity readings.
-- Required concepts: JOIN, ORDER BY, LIMIT.
SELECT
    -- TODO
FROM SensorReading sr
-- TODO
ORDER BY
    -- TODO: humidity descending
LIMIT 10
;

-- 4. Readings outside the comfort profile.
-- Required concepts: JOIN, CASE.
SELECT
    -- TODO: location and reading fields
    -- TODO: CASE expression describing too cold, too hot, too dry, or too humid
FROM SensorReading sr
-- TODO: join Device, Location, and ComfortProfile
WHERE
    -- TODO: any value outside the comfort profile
;

-- 5. Number of readings per device per hour.
-- Required concepts: strftime(), COUNT, GROUP BY.
SELECT
    -- TODO
FROM SensorReading sr
-- TODO
GROUP BY
    -- TODO: device and hour
;

-- 6. Pressure trend per location.
-- Required concepts: window function LAG().
SELECT
    -- TODO: location
    -- TODO: measured_at
    -- TODO: pressure_hpa
    -- TODO: pressure_hpa - previous pressure
FROM (
    SELECT
        -- TODO
        LAG(pressure_hpa) OVER (
            PARTITION BY -- TODO: device or location
            ORDER BY measured_at
        ) AS previous_pressure_hpa
    FROM SensorReading sr
    -- TODO: join Device and Location
)
ORDER BY
    -- TODO
;
