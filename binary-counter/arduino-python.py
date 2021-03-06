import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
pins=[21,20,16,12,7,8,25,24]
arduino_pins=[2,3,4,5,6,7,8,9]
for i in pins:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
arduino = serial.Serial('/dev/ttyACM0', 2000000)
button_pin = 23
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_send_pin = 18
GPIO.setup(button_send_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    i = 0
    j=0
    if not GPIO.input(button_pin):
        for i in range(0,255):
            while GPIO.input(button_send_pin):
                print "esperando a enviar"
                time.sleep(1)
            serial_string = ""
            for j in range(0,8):
                if ( ( (i >> j) & 1 )  == 1 ):
                    GPIO.output(pins[j],1)
                    serial_string += str(arduino_pins[j]) + ",1-"
                else:
                    GPIO.output(pins[j],0)
                    serial_string += str(arduino_pins[j]) + ",0-"
            arduino.write(serial_string.encode())
            print serial_string
            time.sleep(2)
