#install RPIO.GPIO lib
#sudo apt-get update
#sudo apt-get install python3-rpi.gpio
import RPi.GPIO
import time
#setting the BCM GPIO Numbering
GPIO.setmode(GPIO,BCM)
#Setting the PWM Pin as pin 18
Servo_Pin=18
#setting the servo_pin as the output
GPIO.setup(Servo_Pin, GPIO.OUT)
#Setting the PWM frequency from 20ms period
pwm_GPIO.PWM(Servo_Pin, 50)
pwm.start(2.0) #Start the PWM with duty cycle of 2 since the angle is 0
def set_servo_angle(angle):
    #Door to open to an angle of 105 degrees
    #Duty Cycle=(angle/18)+2.0
    #OPENING THE DOOR TO 105 degrees
    #Duty cycle=(105/18)+2.0=7.8
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(Servo_Pin, False)
    pwm.ChangeDutyCycle(0)
    try:
        while True:
            #Sweeping from 0 to 180 degrees
            for angle in range(0, 181,1):
                set_servo_angle(angle)
                time.sleep(0.01)
                #sweeping from 180 to 0 degrees(Reversing the Direction)
                for angle in range(180, -1, -1):
                    set_servo_angle(angle)
                    time.sleep(0.01)
                except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
#On miniconda prompt, type
#sudo Python3 MG90S Control.py



    
