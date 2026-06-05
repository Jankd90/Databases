-- Tutorial 2 climate view and index starters.
-- Fill in the missing SELECT logic and choose indexes based on your own query patterns.

DROP VIEW IF EXISTS DailyClimateSummary;

CREATE VIEW DailyClimateSummary AS
SELECT
    -- TODO: date extracted from measured_at AS reading_date
    -- TODO: location name
    -- TODO: average temperature
    -- TODO: average humidity
    -- TODO: average pressure
    -- TODO: number of readings
FROM SensorReading sr
-- TODO: join Device
-- TODO: join Location
GROUP BY
    -- TODO: date and location
;

-- TODO: create an index that helps time range queries.
-- CREATE INDEX IF NOT EXISTS idx_sensorreading_measured_at ON SensorReading(...);

-- TODO: create an index that helps joining readings to devices.
-- CREATE INDEX IF NOT EXISTS idx_sensorreading_device_id ON SensorReading(...);

-- TODO: create an index that helps finding devices by location.
-- CREATE INDEX IF NOT EXISTS idx_device_location_id ON Device(...);
