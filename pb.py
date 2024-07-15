import RPi.GPIO as GPIO
import time

# Pin Definitions
Button_Pin = 17
Servo_Pin = 18
Solenoid_Pin = 24


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Servo_Pin, GPIO.OUT)
GPIO.setup(Solenoid_Pin, GPIO.OUT)

# Function to operate the door mechanism
def operate_door():
    # Simulate door closing and locking
    print("Closing and locking the door...")
    GPIO.output(Servo_Pin, GPIO.HIGH)  # Operate servo to close the door
    time.sleep(2)  # Adjust delay as needed for servo operation time
    GPIO.output(Solenoid_Pin, GPIO.HIGH)  # Lock the door with solenoid
    time.sleep(1)  # Adjust delay as needed for solenoid operation
    GPIO.output(Servo_Pin, GPIO.LOW)  # Turn off servo

def unlock_door():
    # Simulate unlocking and opening the door
    print("Unlocking and opening the door...")
    GPIO.output(Solenoid_Pin, GPIO.LOW)  # Unlock the door with solenoid
    time.sleep(1)  # Adjust delay as needed for solenoid operation
    # Add code to operate servo to open the door if needed

try:
    while True:
        button_state = GPIO.input(Button_Pin)
        
        if button_state == GPIO.LOW:  # Button pressed
            operate_door()  # Close and lock the door
            time.sleep(0.2)  # Debounce delay
        
        # You can add more conditions here for different actions based on requirements
        
        time.sleep(0.1)  # Small delay to save CPU resources

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()