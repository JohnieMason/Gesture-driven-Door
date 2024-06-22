import RPi.GPIO
import time
#Setting solenoid pin
Solenoid_Pin=24
GPIO.setmode(GPIO.BCM)
GPIO.output(Solenoid_Pin, GPIO.OUT) #Setting the pin as output
try:
    while True:
        GPIO.output(24, GPIO.HIGH) #locking the Door
        Print("Door Locking")
        time.sleep(0.5)
        #Unlocking the door
        GPIO.output(24, GPIO.LOW)
        Print("Door Unlocking")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Program interrupted by the user")
finally:
    GPIO.cleanup(0)
    
