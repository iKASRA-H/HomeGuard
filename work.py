#! /usr/bin/python
import serial
import time
import os
os.system("python3 bt.py &")
data=""
flag=0
bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=38400)
print("Bluetooth connected")
while data=="":
	data = bluetoothSerial.readline()
	print(data)
	time.sleep(1)

os.system("python3 pic2.py")
