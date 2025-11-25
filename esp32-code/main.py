import machine
import time
from machine import Pin, I2C
import socket
import bme280

# Pins
sda_pin = 19
scl_pin = 18

# Server
server_ip = "192.168.43.95"
server_port = 5000

# I2C
i2c = I2C(sda=Pin(sda_pin), scl=Pin(scl_pin))
print("I2C scan:", [hex(a) for a in i2c.scan()])

# Sensor
bme = bme280.BME280(i2c=i2c, address=0x76)


def send_data(data):
    try:
        sock = socket.socket()
        sock.connect((server_ip, server_port))
        sock.sendall(data.encode())
        sock.close()
        print("Data sent")
    except Exception as e:
        print("Send error:", e)


def main():
    while True:
        try:
            t = bme.temperature[:-1]       # remove "C"
            h = bme.humidity[:-1]         # remove "%"
            p = bme.pressure[:-3]         # remove "hPa"

            data = f"Temperature: {t}, Humidity: {h}, Pressure: {p}"
            print(data)

            send_data(data)
            time.sleep(1)

        except Exception as e:
            print("Sensor read error:", e)


main()

