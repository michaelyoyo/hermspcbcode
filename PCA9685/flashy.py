# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 0  # Min pulse length out of 4096
servo_max = 4096  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(600)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, 4095)
    pwm.set_pwm(1, 0, 4095)
    pwm.set_pwm(2, 1024, 4095)
    pwm.set_pwm(3, 256, 4095)
    pwm.set_pwm(4, 3072, 4095)
    time.sleep(0.25)
    pwm.set_pwm(0, 0, 4095)
    pwm.set_pwm(1, 1024, 4095)
    pwm.set_pwm(2, 1024, 4095)
    pwm.set_pwm(3, 1024, 4095)
    pwm.set_pwm(4, 128, 4095)
    time.sleep(0.25)
    pwm.set_pwm(0, 1024, 4095)
    pwm.set_pwm(1, 0, 4095)
    pwm.set_pwm(2, 1024, 4095)
    pwm.set_pwm(3, 256, 4095)
    pwm.set_pwm(4, 3072, 4095)
    time.sleep(0.25)
    pwm.set_pwm(0, 1024, 4095)
    pwm.set_pwm(1, 1024, 4095)
    pwm.set_pwm(2, 1024, 4095)
    pwm.set_pwm(3, 1024, 4095)
    pwm.set_pwm(4, 128, 4095)
    time.sleep(0.25)	
