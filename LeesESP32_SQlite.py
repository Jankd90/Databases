import socket
import sqlite3

# Network parameters
server_ip = "0.0.0.0"
server_port = 5000

# SQLite database file
database_file = r"C:\Users\jgm_6\OneDrive - Hanzehogeschool Groningen\Education\Databases\databases\databases\uitwerkingen Db\Databases 18-6-2024\PC script\PCpythonprogram\bme280data.db"

# --- create database and table if not exist ---
def init_db():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bme280data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Temperatuur REAL,
            Vochtigheid REAL,
            Druk REAL,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# --- insert measurement ---
def insert_data(temperature, humidity, pressure):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bme280data (Temperatuur, Vochtigheid, Druk)
            VALUES (?, ?, ?)
        """, (temperature, humidity, pressure))
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
            fields = data.split(", ")
            temperature = float(fields[0].split(": ")[1].split(" ")[0])
            humidity = float(fields[1].split(": ")[1].split(" ")[0])
            pressure = float(fields[2].split(": ")[1].split(" ")[0])
            insert_data(temperature, humidity, pressure)
        except Exception as e:
            print("Parsing or DB error:", e)

        conn.close()
        print("Connection closed\n")

if __name__ == "__main__":
    main()
