#!/usr/bin/python

import phprobe
import time

ph = phprobe.pH_probe()
ph.find(1)
ph.setLED(1)

print "Starting readings..."

try:
	while 1:
		print ph.pHRead()
		time.sleep(1)
except KeyboardInterrupt:
	del ph
	print "Stopped"
