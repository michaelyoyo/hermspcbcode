import time
import Adafruit_ADS1x15
import Adafruit_PCA9685
from __future__ import division

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
adc = Adafruit_ADS1x15.ADS1115()

motor_speed = 0
pwm.set_pwm_freq(600)
GAIN = 1
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
while True:
	if(motor_speed % 20):
		pwm.set_pwm_freq(5, (4096-motor_speed*409.6), 4096)
		pwm.set_pwm_freq(4, 2048, 4096)
	else:
		pwm.set_pwm_freq(4, 4096, 4096)
	values = [0]*4
	for i in range(4):
		values[i] = adc.read_adc(i, gain=GAIN)
	print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
	motor_speed += 5
	if(motor_speed == 100):
		motor_speed = 0
	time.sleep(0.25)