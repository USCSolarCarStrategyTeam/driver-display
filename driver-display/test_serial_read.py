#!/usr/bin/env python
import time
import serial
import threading

# class SerialThread(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.serial_port = serial.Serial('/dev/ttyUSB0', 9600)


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# while 1:
x = ser.readline().decode('utf-8')
data = x.split()
print(x)

# speed
if data[0] == 0:
    speed = data[1]
# range
elif data[0] == 1:
    range = data[1]