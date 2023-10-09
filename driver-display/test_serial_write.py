#!/usr/bin/env python
import serial

ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser.write('Hello World\n'.encode('utf-8'))

ser.close()