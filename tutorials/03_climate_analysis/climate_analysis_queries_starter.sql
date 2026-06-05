-- Tutorial 3 starter: climate analysis queries for climate_station.db.

-- 1. Locations outside comfort profile most often.
SELECT
    -- TODO: location name
    -- TODO: number of readings
    -- TODO: number of comfort violations
    -- TODO: percentage outside comfort range
FROM SensorReading sr
-- TODO: join Device, Location, ComfortProfile
GROUP BY
    -- TODO: location
ORDER BY
    -- TODO: highest violation percentage first
;

-- 2. Average climate by hour of day.
SELECT
    -- TODO: hour extracted from measured_at
    -- TODO: average temperature
    -- TODO: average humidity
    -- TODO: average pressure
FROM SensorReading
GROUP BY
    -- TODO: hour
ORDER BY
    -- TODO: hour
;

-- 3. Pressure trend using LAG.
SELECT
    -- TODO: device or location name
    -- TODO: measured_at
    -- TODO: pressure_hpa
    -- TODO: pressure_hpa - previous pressure AS pressure_change_hpa
FROM (
    SELECT
        -- TODO
        LAG(pressure_hpa) OVER (
            PARTITION BY -- TODO: device_id
            ORDER BY measured_at
        ) AS previous_pressure_hpa
    FROM SensorReading sr
    -- TODO: join Device and Location
)
ORDER BY
    -- TODO
;

-- 4. Daily indoor climate summary.
SELECT
    -- TODO: date
    -- TODO: location name
    -- TODO: min, avg, max temperature
    -- TODO: avg humidity
    -- TODO: avg pressure
FROM SensorReading sr
-- TODO: join Device and Location
WHERE
    -- TODO: indoor locations only, if your location_type supports it
GROUP BY
    -- TODO: date and location
ORDER BY
    -- TODO
;

-- 5. Similar room behavior by average temperature and humidity.
SELECT
    -- TODO: first location
    -- TODO: second location
    -- TODO: absolute difference in average temperature
    -- TODO: absolute difference in average humidity
FROM (
    SELECT
        -- TODO: location id, name, avg temperature, avg humidity
    FROM SensorReading sr
    -- TODO: join Device and Location
    GROUP BY
        -- TODO: location
) room_a
JOIN (
    SELECT
        -- TODO: same summary for room_b
    FROM SensorReading sr
    -- TODO: join Device and Location
    GROUP BY
        -- TODO: location
) room_b
    -- TODO: compare each pair once
ORDER BY
    -- TODO: most similar first
;
