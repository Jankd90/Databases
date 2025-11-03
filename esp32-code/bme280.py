# bme280.py
# MicroPython driver for BME280 sensor (ESP32-compatible)
# Supports temperature, pressure, and humidity via I2C

import time
from ustruct import unpack

class BME280:
    def __init__(self, i2c, address=0x76):
        self.i2c = i2c
        self.address = address
        self._load_calibration()
        self._configure()

    def _read(self, register, length=1):
        return self.i2c.readfrom_mem(self.address, register, length)

    def _write(self, register, data):
        self.i2c.writeto_mem(self.address, register, bytes([data]))

    def _load_calibration(self):
        calib = self._read(0x88, 26) + self._read(0xE1, 7)
        self.dig_T1, self.dig_T2, self.dig_T3 = unpack("<Hhh", calib[0:6])
        self.dig_P1, self.dig_P2, self.dig_P3, self.dig_P4, self.dig_P5, \
        self.dig_P6, self.dig_P7, self.dig_P8, self.dig_P9 = unpack("<Hhhhhhhhh", calib[6:24])
        self.dig_H1 = calib[25]
        self.dig_H2, self.dig_H3 = unpack("<hB", calib[26:29])
        e4, e5, e6 = calib[29:32]
        self.dig_H4 = (e4 << 4) | (e5 & 0x0F)
        self.dig_H5 = (e6 << 4) | (e5 >> 4)
        self.dig_H6 = calib[32]
        self.t_fine = 0

    def _configure(self):
        self._write(0xF2, 0x01)  # Humidity oversampling x1
        self._write(0xF4, 0x27)  # Temp/pressure oversampling x1, mode normal
        self._write(0xF5, 0xA0)  # Standby 1000 ms, filter off

    def _read_raw_data(self):
        data = self._read(0xF7, 8)
        pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
        hum_raw = (data[6] << 8) | data[7]
        return temp_raw, pres_raw, hum_raw

    def read_compensated_data(self):
        temp_raw, pres_raw, hum_raw = self._read_raw_data()

        # Temperature compensation
        var1 = (((temp_raw >> 3) - (self.dig_T1 << 1)) * self.dig_T2) >> 11
        var2 = (((((temp_raw >> 4) - self.dig_T1) *
                  ((temp_raw >> 4) - self.dig_T1)) >> 12) *
                self.dig_T3) >> 14
        self.t_fine = var1 + var2
        temperature = (self.t_fine * 5 + 128) >> 8

        # Pressure compensation
        var1 = self.t_fine - 128000
        var2 = var1 * var1 * self.dig_P6
        var2 = var2 + ((var1 * self.dig_P5) << 17)
        var2 = var2 + (self.dig_P4 << 35)
        var1 = ((var1 * var1 * self.dig_P3) >> 8) + ((var1 * self.dig_P2) << 12)
        var1 = (((1 << 47) + var1) * self.dig_P1) >> 33
        if var1 == 0:
            pressure = 0
        else:
            p = 1048576 - pres_raw
            p = (((p << 31) - var2) * 3125) // var1
            var1 = (self.dig_P9 * (p >> 13) * (p >> 13)) >> 25
            var2 = (self.dig_P8 * p) >> 19
            pressure = ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)

        # Humidity compensation
        h = self.t_fine - 76800
        h = (((((hum_raw << 14) - (self.dig_H4 << 20) - (self.dig_H5 * h)) + 16384) >> 15)
             * (((((((h * self.dig_H6) >> 10) * (((h * self.dig_H3) >> 11) + 32768)) >> 10)
                  + 2097152) * self.dig_H2 + 8192) >> 14))
        h = h - (((((h >> 15) * (h >> 15)) >> 7) * self.dig_H1) >> 4)
        h = max(0, min(h >> 12, 419430400))
        humidity = h >> 12

        return temperature / 100.0, pressure / 25600.0, humidity / 1024.0

    def values(self):
        t, p, h = self.read_compensated_data()
        return ("%.2f C" % t, "%.2f hPa" % p, "%.2f %%" % h)
    
    def temperature(self):
        t, _, _ = self.read_compensated_data()
        return t

    def pressure(self):
        _, p, _ = self.read_compensated_data()
        return p

    def humidity(self):
        _, _, h = self.read_compensated_data()
        return h

