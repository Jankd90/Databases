-- Tutorial 4 seed data for a weather station or smart-home indoor climate database.

PRAGMA foreign_keys = ON;

INSERT INTO Location (location_id, name, location_type, floor, notes)
VALUES
    (1, 'Living Room', 'indoor_room', '0', 'Main smart-home sensor location'),
    (2, 'Bedroom', 'indoor_room', '1', 'Night comfort monitoring'),
    (3, 'Balcony', 'outdoor', '0', 'Outdoor weather comparison');

INSERT INTO Device (device_id, device_name, device_type, location_id, installed_at)
VALUES
    (1, 'ESP32 BME280 Living', 'ESP32_BME280', 1, '2026-06-01 09:00:00'),
    (2, 'ESP32 BME280 Bedroom', 'ESP32_BME280', 2, '2026-06-01 09:30:00'),
    (3, 'ESP32 BME280 Outdoor', 'ESP32_BME280', 3, '2026-06-01 10:00:00');

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
    (2, 2, 17.0, 22.0, 35.0, 60.0),
    (3, 3, -10.0, 35.0, 20.0, 90.0);

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
    (3, 1, '2026-06-04 10:00:00', 25.1, 43.9, 1012.8),
    (4, 2, '2026-06-04 08:00:00', 18.5, 55.0, 1013.3),
    (5, 2, '2026-06-04 09:00:00', 18.9, 62.5, 1013.0),
    (6, 3, '2026-06-04 08:00:00', 17.5, 68.4, 1013.8),
    (7, 3, '2026-06-04 09:00:00', 18.1, 66.9, 1013.5);
