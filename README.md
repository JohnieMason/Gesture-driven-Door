# GPIO-Control.txt
#How to Control GPIO pins of RPi
import RPi.GPIO as GPIO                                GPIO
import time
#setting BCM Numbering
GPIO.setmode(GPIO.BCM)
#set the pin to the output
GPIO.setup(27, GPIO.OUT)
#Controlling the pin
try:
 while True:
  GPIO.output(27, GPIO.HIGH)
  print("GPIO is ON")
  time.sleep(1)
  GPIO.output(27, GPIO.LOW)
  print("GPIO is OFF")
  time.sleep(1)
except KeyboardInterrupt:
 print("Program terminated")
finally:
 GPIO.cleanup()
