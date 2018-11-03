from __future__ import division
import time
import Adafruit_ADS1x15
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
adc = Adafruit_ADS1x15.ADS1115()

motor_speed = 0
pwm.set_pwm_freq(600)
GAIN = 1
pwm.set_pwm(0,0,4095)
pwm.set_pwm(1,0,4095)
pwm.set_pwm(2,0,4095)
pwm.set_pwm(3,0,4095)
pwm.set_pwm(4,0,4095)
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} |'.format(*range(2)))
print('-' * 37)
while True:
    # print motor_speed%20
    if((motor_speed % 20) == 0):
        pwm_start = int(4096-motor_speed*409.6)
        pwm.set_pwm(8, pwm_start, 4095)
        print pwm_start
        pwm.set_pwm(3, 1024, 4095)
        # print "ping"
    else:
        pwm.set_pwm(3, 0, 4095)
        # print "pong"
    values = [0]*2
    for i in range(2):
        values[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} |'.format(*values))
    motor_speed += 5
    if(motor_speed == 100):
        motor_speed = 0
    time.sleep(0.25)
