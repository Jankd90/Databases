# bme280.py — MicroPython BME280 driver (property version)
# Compatible with ESP32, ESP8266, Raspberry Pi Pico

import time
from ustruct import unpack
from machine import I2C

class BME280:
    def __init__(self, i2c=None, address=0x76):
        self.i2c = i2c
        self.address = address
        self._load_calibration()
        # Humidity oversampling x1
        self.i2c.writeto_mem(self.address, 0xF2, b'\x01')
        # Temp and pressure oversampling x1, mode normal
        self.i2c.writeto_mem(self.address, 0xF4, b'\x27')
        # Standby 1000ms
        self.i2c.writeto_mem(self.address, 0xF5, b'\xA0')

        self._t_fine = 0
        self._temperature = None
        self._pressure = None
        self._humidity = None

    def _load_calibration(self):
        calib = self.i2c.readfrom_mem(self.address, 0x88, 26)
        self.dig_T1, self.dig_T2, self.dig_T3, \
        self.dig_P1, self.dig_P2, self.dig_P3, self.dig_P4, self.dig_P5, \
        self.dig_P6, self.dig_P7, self.dig_P8, self.dig_P9, self.dig_H1 = \
            unpack('<HhhHhhhhhhhhB', calib)

        calib = self.i2c.readfrom_mem(self.address, 0xE1, 7)
        self.dig_H2, self.dig_H3, e4, e5, e6, self.dig_H6 = unpack('<hBbbbB', calib)
        self.dig_H4 = (e4 << 4) | (e5 & 0x0F)
        self.dig_H5 = (e6 << 4) | (e5 >> 4)

    def _read_raw_data(self):
        data = self.i2c.readfrom_mem(self.address, 0xF7, 8)
        pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
        hum_raw = (data[6] << 8) | data[7]
        return temp_raw, pres_raw, hum_raw

    def _compensate(self):
        adc_T, adc_P, adc_H = self._read_raw_data()

        # Temperature
        var1 = (((adc_T / 16384.0) - (self.dig_T1 / 1024.0)) * self.dig_T2)
        var2 = (((adc_T / 131072.0) - (self.dig_T1 / 8192.0)) ** 2) * self.dig_T3
        self._t_fine = int(var1 + var2)
        self._temperature = (var1 + var2) / 5120.0

        # Pressure
        var1 = self._t_fine / 2.0 - 64000.0
        var2 = var1 * var1 * self.dig_P6 / 32768.0
        var2 = var2 + var1 * self.dig_P5 * 2.0
        var2 = var2 / 4.0 + self.dig_P4 * 65536.0
        var1 = (self.dig_P3 * var1 * var1 / 524288.0 + self.dig_P2 * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self.dig_P1
        if var1 == 0:
            self._pressure = 0
        else:
            p = 1048576.0 - adc_P
            p = ((p - var2 / 4096.0) * 6250.0) / var1
            var1 = self.dig_P9 * p * p / 2147483648.0
            var2 = p * self.dig_P8 / 32768.0
            self._pressure = (p + (var1 + var2 + self.dig_P7) / 16.0) / 100.0

        # Humidity
        h = self._t_fine - 76800.0
        h = (adc_H - (self.dig_H4 * 64.0 + self.dig_H5 / 16384.0 * h)) * (
            self.dig_H2 / 65536.0 * (1.0 + self.dig_H6 / 67108864.0 * h *
            (1.0 + self.dig_H3 / 67108864.0 * h))
        )
        self._humidity = h * (1.0 - self.dig_H1 * h / 524288.0)
        if self._humidity > 100:
            self._humidity = 100
        elif self._humidity < 0:
            self._humidity = 0

    @property
    def temperature(self):
        self._compensate()
        return self._temperature

    @property
    def pressure(self):
        self._compensate()
        return self._pressure

    @property
    def humidity(self):
        self._compensate()
        return self._humidity
