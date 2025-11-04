# Getting Started with ESP32, MicroPython and SQlite Database

This repository contains code for an ESP32-based data acquisition system using a BME280 sensor and a Python host server with SQLite. The ESP32 reads environmental data (temperature, humidity, pressure) and transmits it to a host computer for database storage.

---

## Requirements

* ESP32 microcontroller
* BME280 sensor (I²C interface)
* Thonny IDE
* Python 3.10+ on host computer
* [DB browser](https://sqlitebrowser.org/)

The Python host uses the following dependencies (see `requirements.txt`):

```
sqlite3
```

---

## 1. Install Thonny IDE

1. Download and install **Thonny** from [https://thonny.org](https://thonny.org).
2. Open Thonny and go to
   **Tools → Options → Interpreter**
3. Select:

   * **Interpreter:** “MicroPython (ESP32)”
   * **Port:** your ESP32 serial port
4. Click **Install or update MicroPython (firmware)** if not already present.

   * Choose your ESP32 model
   * Follow on-screen instructions to flash MicroPython firmware

---

## 2. Configure ESP32

1. Edit `secure.txt` to include your WiFi credentials (line 1 = SSID, line 2 = password).

2. Add your computer’s IPv4 address (found via ipconfig in the terminal) to the server_ip field in main.py

3. Connect ESP32 via USB.

4. Open Thonny’s **Files** pane and copy the following files to the ESP32:

   * `boot.py`
   * `main.py`
   * `bme280.py`
   * `secure.txt` (contains WiFi SSID and password)



When powered, `boot.py` automatically connects to WiFi using these credentials.

---

## 3. Configure Thonny for ESP32

* In Thonny’s **Shell**, you should see:

  ```
  Connect to WiFi: ('192.168.x.x', '255.255.255.0', '192.168.x.x', '8.8.8.8')
  ```

  This confirms network connection.
* Run `main.py` — it will start reading sensor data and transmitting it via TCP to the host.

---

## 4. Host Python Server (Data Storage)

1. Edit `database_file = r"C:\[YOUR_PATH]\bme280data.db"` to include your path.

2. Run the host server on your PC:

```bash
python LeesESP32_SQlite.py
```

This script:

* Initializes an SQLite database (`bme280data.db`)
* Listens on `0.0.0.0:5000`
* Receives and stores data from the ESP32

---

## 5. Learn More About Databases

A detailed introduction to database concepts and SQL can be found here:
👉 [Database Reader](https://jankd90.github.io/Databases/intro.html)

---

## File Overview

| File                  | Description                                |
| --------------------- | ------------------------------------------ |
| `boot.py`             | Connects ESP32 to WiFi                     |
| `main.py`             | Reads BME280 sensor and sends data         |
| `bme280.py`           | Sensor driver (MicroPython)                |
| `secure.txt`          | WiFi credentials                           |
| `LeesESP32_SQlite.py` | Host-side data receiver and SQLite handler |
| `requirements.txt`    | Python dependencies                        |

---

## Notes

* Ensure both devices share the same WiFi network.
* If the ESP32 fails to connect, verify the SSID/password and network compatibility (2.4 GHz).
* The data is transmitted as plain text and can be adapted for secure communication if required.
