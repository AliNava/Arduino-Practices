import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
pins=[21,20,16,12,7,8,25,24]
for i in pins:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
#arduino = serial.Serial('/dev/ttyACM0', 2304000)
button_pin = 23
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    i = 0
    j=0
    if not GPIO.input(button_pin):
        for i in range(0,255):
            for j in range(0,8):
                if ( ( (i >> j) & 1 )  == 1 ):
                    print((str(pins[j]) + ",1").encode())
				    #arduino.write((str(pins[j]) + ",1").encode())
                    GPIO.output(pins[j],1)
                else:
                    print((str(pins[j]) + ",0").encode())
				    #arduino.write((str(pins[j]) + ",0").encode())
                    GPIO.output(pins[j],0)
                time.sleep(1)
            print("--------------     ")
