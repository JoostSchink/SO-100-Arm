import RPi.GPIO as GPIO
import time

# Use Broadcom pin numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins (update these to your wiring)
STEP_PIN = 18  # GPIO pin connected to TMC2310 STEP input
DIR_PIN = 23   # GPIO pin connected to TMC2310 DIR input

# Set up the GPIO pins as outputs
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set motor direction (GPIO.HIGH or GPIO.LOW)
GPIO.output(DIR_PIN, GPIO.HIGH)

# Define the number of steps and delay between steps
num_steps = 200        # Change this to how many steps you need
step_delay = 0.001     # Delay in seconds (adjust for your speed)

# Pulse the step pin to move the motor
for step in range(num_steps):
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(step_delay)
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(step_delay)

# Clean up GPIO settings
GPIO.cleanup()
