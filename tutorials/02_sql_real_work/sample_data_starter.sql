-- Tutorial 2 fallback starter data.
-- Use this if the ESP32/BME280 hardware is not available during class.
-- Run this after your generated climate station schema has been loaded.

PRAGMA foreign_keys = ON;

-- TODO: adjust columns if your ChartDB design uses different names.

INSERT INTO Location (location_id, name, location_type)
VALUES
    (1, 'Living Room', 'indoor_room'),
    (2, 'Balcony', 'outdoor');

INSERT INTO Device (device_id, device_name, device_type, location_id)
VALUES
    (1, 'ESP32 BME280 A', 'ESP32_BME280', 1),
    (2, 'ESP32 BME280 B', 'ESP32_BME280', 2);

INSERT INTO ComfortProfile (
    profile_id,
    location_id,
    min_temperature_c,
    max_temperature_c,
    min_humidity_percent,
    max_humidity_percent
)
VALUES
    (1, 1, 19.0, 24.0, 35.0, 60.0),
    (2, 2, -10.0, 35.0, 20.0, 90.0);

-- TODO: add at least 20 readings across multiple hours or days.
INSERT INTO SensorReading (
    reading_id,
    device_id,
    measured_at,
    temperature_c,
    humidity_percent,
    pressure_hpa
)
VALUES
    (1, 1, '2026-06-04 08:00:00', 20.8, 45.2, 1013.4),
    (2, 1, '2026-06-04 09:00:00', 21.4, 44.7, 1013.1),
    (3, 1, '2026-06-04 10:00:00', 22.1, 43.9, 1012.8),
    (4, 2, '2026-06-04 08:00:00', 17.5, 68.4, 1013.8),
    (5, 2, '2026-06-04 09:00:00', 18.1, 66.9, 1013.5);
