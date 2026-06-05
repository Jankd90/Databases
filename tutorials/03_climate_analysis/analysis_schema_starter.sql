-- Tutorial 3 starter: analysis schema for climate_station.db.
-- Run after Tutorial 2 has created Location, Device, SensorReading, and ComfortProfile.

PRAGMA foreign_keys = ON;

-- Optional hierarchy: a building contains floors, floors contain rooms,
-- or a weather station contains outdoor sensor positions.
CREATE TABLE IF NOT EXISTS LocationHierarchy (
    parent_location_id INTEGER NOT NULL,
    child_location_id INTEGER NOT NULL,
    relationship_type TEXT NOT NULL DEFAULT 'contains',
    PRIMARY KEY (parent_location_id, child_location_id),
    FOREIGN KEY (parent_location_id) REFERENCES Location(location_id),
    FOREIGN KEY (child_location_id) REFERENCES Location(location_id),
    CHECK (parent_location_id <> child_location_id)
);

CREATE TABLE IF NOT EXISTS AlertRule (
    rule_id INTEGER PRIMARY KEY,
    location_id INTEGER NOT NULL,
    metric TEXT NOT NULL CHECK (metric IN ('temperature_c', 'humidity_percent', 'pressure_hpa')),
    operator TEXT NOT NULL CHECK (operator IN ('<', '>', '<=', '>=')),
    threshold_value REAL NOT NULL,
    severity TEXT NOT NULL CHECK (severity IN ('info', 'warning', 'critical')),
    message TEXT NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 1 CHECK (enabled IN (0, 1)),
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

CREATE TABLE IF NOT EXISTS AlertEvent (
    alert_event_id INTEGER PRIMARY KEY,
    rule_id INTEGER NOT NULL,
    reading_id INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at TEXT,
    FOREIGN KEY (rule_id) REFERENCES AlertRule(rule_id),
    FOREIGN KEY (reading_id) REFERENCES SensorReading(reading_id)
);

-- TODO: insert at least one parent location and connect existing rooms/sensor locations to it.
-- TODO: insert at least four alert rules for temperature and humidity.
-- TODO: generate AlertEvent rows from SensorReading rows that violate your rules.
