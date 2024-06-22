import RPi.GPIO as GPIO
import time

#setting BCM NUmbering
GPIO.setmode(GPIO.BCM)
#setting pin 3 as the output
GPIO.setup(2,GPIO.OUT)
try:
    while True:
        #Set the output high
        GPIO.output(2,GPIO.HIGH)
        print("GPIO2 IS ON")
        sleep.time(1)
        #set the output low
        GPIO.output(2,GPIO.LOW)
        print("GPIO2 is OFF")
        sleep.time(1)
except KeyboardInterrupt:
    print("program terminated")
finally:
    #clean up the GPIO settings
    GPIO.cleanup()


