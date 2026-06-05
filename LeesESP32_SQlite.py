import socket
import sqlite3

# Network parameters
server_ip = "0.0.0.0"
server_port = 5000

# SQLite database file
database_file = r"climate_station.db"

# Default records used when the database is empty.
default_location_id = 1
default_device_id = 1

# --- create database and table if not exist ---
def init_db():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Location (
            location_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            location_type TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Device (
            device_id INTEGER PRIMARY KEY,
            device_name TEXT NOT NULL,
            device_type TEXT NOT NULL,
            location_id INTEGER NOT NULL,
            FOREIGN KEY (location_id) REFERENCES Location(location_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SensorReading (
            reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER NOT NULL,
            measured_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            temperature_c REAL NOT NULL,
            humidity_percent REAL NOT NULL,
            pressure_hpa REAL NOT NULL,
            FOREIGN KEY (device_id) REFERENCES Device(device_id)
        )
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO Location (location_id, name, location_type)
        VALUES (?, ?, ?)
    """, (default_location_id, "Living Room", "indoor_room"))
    cursor.execute("""
        INSERT OR IGNORE INTO Device (device_id, device_name, device_type, location_id)
        VALUES (?, ?, ?, ?)
    """, (default_device_id, "ESP32 BME280 A", "ESP32_BME280", default_location_id))
    conn.commit()
    conn.close()

# --- insert measurement ---
def insert_data(temperature, humidity, pressure):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("""
            INSERT INTO SensorReading (
                device_id,
                temperature_c,
                humidity_percent,
                pressure_hpa
            )
            VALUES (?, ?, ?, ?)
        """, (default_device_id, temperature, humidity, pressure))
        conn.commit()
        conn.close()
        print("Data inserted successfully")
    except Exception as e:
        print("Error inserting data:", e)

# --- main server loop ---
def main():
    init_db()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_ip, server_port))
    sock.listen(5)
    print(f"Listening on {server_ip}:{server_port}")

    while True:
        conn, addr = sock.accept()
        print("Connected from:", addr)

        data = conn.recv(1024).decode()
        print("Received:", data)

        try:
            fields = {}
            for part in data.split(","):
                key, value = part.strip().split(":", maxsplit=1)
                fields[key.strip().lower()] = float(value.strip().split(" ")[0])

            temperature = fields["temperature"]
            humidity = fields["humidity"]
            pressure = fields["pressure"]
            insert_data(temperature, humidity, pressure)
        except Exception as e:
            print("Parsing or DB error:", e)

        conn.close()
        print("Connection closed\n")

if __name__ == "__main__":
    main()
