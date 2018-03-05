import time
import serial
pins=[2,3,4,5,6,7,8,9]
arduino = serial.Serial('/dev/ttyACM0', 2304000)
while True:
	i = 0
	j=0
	for i in range(0,255):
		for j in range(0,8):
			if ( ( (i >> j) & 1 )  == 1 ):
				print((str(pins[j]) + ",1").encode())
				arduino.write((str(pins[j]) + ",1").encode())
			else:
				print((str(pins[j]) + ",0").encode())
				arduino.write((str(pins[j]) + ",0").encode())
			time.sleep(1)
		print("-------------")
