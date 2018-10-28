#!/usr/bin/python

import max31865
import time

temp = max31865.MAX31865()
print "Checking Faults"
temp.faultReset()
fault = temp.faultDetect()
current_temp = temp.getTemp()
if current_temp < 0:
	print current_temp
if fault != 0:
	print "Fault Detected: " + hex(fault)
	quit()
print "Starting Read"
temp.startAutoConversion()
while True:
	print 32+(temp.getTemp()*(9/5.0))
	time.sleep(1)
