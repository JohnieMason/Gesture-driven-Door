import RPi.GPIO as GPIO
import time

# Configure GPIO pin numbers
button_pin = 17  # Push button input pin
servo_pin = 18  # PWM output pin for servo motor
solenoid_pin = 23  # Output pin for solenoid

# Set GPIO mode and initial state
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(solenoid_pin, GPIO.OUT)

# Create PWM instance for the servo motor
servo_pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency for servo motor

# Initialize door status flags
door_open = False
door_locked = True

# Function to close and lock the door
def close_and_lock_door():
    global door_open, door_locked
    
    if door_open and not door_locked:
        print("Closing and locking the door.")
        # Move servo motor to close the door
        servo_pwm.start(10)  # Change duty cycle for closed position
        time.sleep(2)  # Wait for the servo to move
        servo_pwm.stop()  # Stop PWM signal

        # Activate the solenoid to lock the door
        GPIO.output(solenoid_pin, GPIO.HIGH)
        time.sleep(3)  # Keep the solenoid activated for 3 seconds
        GPIO.output(solenoid_pin, GPIO.LOW)  # Deactivate the solenoid

        door_open = False
        door_locked = True
    else:
        print("The door is already closed and locked.")

# Function to unlock and open the door
def unlock_and_open_door():
    global door_open, door_locked
    
    if not door_open and door_locked:
        print("Unlocking and opening the door.")
        # Deactivate the solenoid to unlock the door
        GPIO.output(solenoid_pin, GPIO.LOW)

        # Move servo motor to open the door
        servo_pwm.start(2.5)  # Change duty cycle for open position
        time.sleep(2)  # Wait for the servo to move
        servo_pwm.stop()  # Stop PWM signal

        door_open = True
        door_locked = False
    else:
        print("The door is already unlocked and open.")

# Event handler for the button press
def button_callback(channel):
    print("Button pressed! Activating emergency override.")
    if door_open:
        close_and_lock_door()
    else:
        unlock_and_open_door()

# Register the event handler for the button press
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    print("Press the button to activate emergency override.")
    while True:
        time.sleep(1)  # Keep the program running

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()



