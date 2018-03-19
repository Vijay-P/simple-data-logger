import serial
import os.path
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

if(not os.path.isfile('dataBase.csv')):
	print("making file")
	with open('dataBase.csv', 'w') as f:
		f.write("time,light,temp\n")
print(os.path.isfile('dataBase.csv'))
while True:
	with open('dataBase.csv', 'a') as f:
		f.write(str(int(round(time.time()*1000)))+","+ser.readline())

