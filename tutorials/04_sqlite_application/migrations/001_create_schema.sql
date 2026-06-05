-- Tutorial 4 migration: climate station application schema.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Location (
    location_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location_type TEXT NOT NULL,
    floor TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS Device (
    device_id INTEGER PRIMARY KEY,
    device_name TEXT NOT NULL,
    device_type TEXT NOT NULL,
    location_id INTEGER NOT NULL,
    installed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

CREATE TABLE IF NOT EXISTS SensorReading (
    reading_id INTEGER PRIMARY KEY,
    device_id INTEGER NOT NULL,
    measured_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temperature_c REAL NOT NULL,
    humidity_percent REAL NOT NULL,
    pressure_hpa REAL NOT NULL,
    FOREIGN KEY (device_id) REFERENCES Device(device_id)
);

CREATE TABLE IF NOT EXISTS ComfortProfile (
    profile_id INTEGER PRIMARY KEY,
    location_id INTEGER NOT NULL,
    min_temperature_c REAL NOT NULL,
    max_temperature_c REAL NOT NULL,
    min_humidity_percent REAL NOT NULL,
    max_humidity_percent REAL NOT NULL,
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

CREATE INDEX IF NOT EXISTS idx_device_location_id ON Device(location_id);
CREATE INDEX IF NOT EXISTS idx_sensorreading_device_id ON SensorReading(device_id);
CREATE INDEX IF NOT EXISTS idx_sensorreading_measured_at ON SensorReading(measured_at);
CREATE INDEX IF NOT EXISTS idx_comfortprofile_location_id ON ComfortProfile(location_id);
