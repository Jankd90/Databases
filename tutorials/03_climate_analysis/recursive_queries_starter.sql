-- Tutorial 3 starter: recursive SQLite queries for climate locations.

PRAGMA foreign_keys = ON;

-- 1. All child locations below a chosen parent.
WITH RECURSIVE location_tree AS (
    SELECT
        -- TODO: parent location id
        -- TODO: child location id
        1 AS depth
    FROM LocationHierarchy
    WHERE
        -- TODO: chosen parent_location_id

    UNION ALL

    SELECT
        -- TODO: next parent
        -- TODO: next child
        location_tree.depth + 1 AS depth
    FROM LocationHierarchy lh
    JOIN location_tree
        -- TODO: continue from the previous child location
)
SELECT
    -- TODO: location names and depth
FROM location_tree
-- TODO: join Location
ORDER BY depth;

-- 2. All readings captured below a chosen parent location.
WITH RECURSIVE location_tree AS (
    SELECT
        -- TODO: child location id
        1 AS depth
    FROM LocationHierarchy
    WHERE
        -- TODO: chosen parent_location_id

    UNION ALL

    SELECT
        -- TODO: child location id
        location_tree.depth + 1 AS depth
    FROM LocationHierarchy lh
    JOIN location_tree
        -- TODO
)
SELECT
    -- TODO: location, device, measured_at, temperature, humidity, pressure
FROM location_tree lt
-- TODO: join Location, Device, SensorReading
ORDER BY
    -- TODO: newest readings first
;

-- 3. Alert counts grouped under a chosen parent location.
WITH RECURSIVE location_tree AS (
    SELECT
        -- TODO: child location id
        1 AS depth
    FROM LocationHierarchy
    WHERE
        -- TODO: chosen parent_location_id

    UNION ALL

    SELECT
        -- TODO
    FROM LocationHierarchy lh
    JOIN location_tree
        -- TODO
)
SELECT
    -- TODO: location name
    -- TODO: alert severity
    -- TODO: count of alerts
FROM location_tree lt
-- TODO: join Location, AlertRule, AlertEvent
GROUP BY
    -- TODO
ORDER BY
    -- TODO
;
