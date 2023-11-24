import serial
import time

ser = serial.Serial('/dev/cu.usbserial-120', 115200, timeout=None)
time.sleep(1)


ser.write(b"0,0,73,-81,-92,20,50,4000,2000")


    

