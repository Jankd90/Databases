#data communication & data processing
#databases
#Peter Kamphuis (kapj) Jos Bos (bosj)
#date: 18 June 2024

import machine
import time
from machine import Pin, I2C
import socket
import bme280

# GPIO pins I2C
sda_pin = 19
scl_pin = 18

# IP-adres and port number of server
server_ip = "192.168.2.9"
server_port = 5000


# Initialisation I2C
i2c = I2C(sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin))
print('I2C scan result:', [hex(addr) for addr in i2c.scan()])

# Initialisation BME280-sensor
bme = bme280.BME280(i2c=i2c, address=0x76)

# Function to send data via socket
def send_data(data):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))
        sock.sendall(data)
        sock.close()
        print("Data send successfully")
    except Exception as e:
        print("Error send data:", e)

# main program
def main():
    try:
        # loop read data from sensor and send data
        while True:
            bme.values()
            temperature = bme.temperature()
            humidity = bme.humidity()
            pressure = bme.pressure()

            data = "Temperatuur: {:.2f} °C, Vochtigheid: {:.2f} %, Druk: {:.2f} hPa".format(temperature, humidity, pressure)
            print(data)
            send_data(data)

            # Wait 1 second to read sensor again
            time.sleep(1)

    except Exception as e:
        print("Error to read BME-280 sensor:", e)

# Start main program
main()

