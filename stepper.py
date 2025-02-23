from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# Define GPIO pins
GPIO_pins = (14, 15, 18)  # Microstep Resolution MS1-MS3 -> GPIO Pins
direction = 20           # Direction -> GPIO Pin
step = 21                # Step -> GPIO Pin

# Declare an instance of the motor class
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

if __name__ == "__main__":
    # Immediately perform 200 steps clockwise.
    # Parameters: motor_go(clockwise, step_type, steps, step_delay, verbose, init_delay)
    mymotortest.motor_go(True, "Full", 200, 0.005, False, 0.05)
    
    # Cleanup GPIO resources if needed.
    GPIO.cleanup()
