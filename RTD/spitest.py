#!/usr/bin/python

import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
print spi.mode
print spi.bits_per_word
print spi.max_speed_hz
spi.max_speed_hz = 1000000
spi.mode = 1
try:
	spi.xfer([0x03,0xFF])
        time.sleep(0.1)
	spi.writebytes([0x80,0xD1])
	spi.xfer2([0x00,0xFF])
	spi.xfer2([0x03,0xFF])
	time.sleep(1)
	while True:
		print spi.xfer([0x01,0x00])
		print spi.xfer([0x02,0x00])
		time.sleep(.1)
    #end while
except KeyboardInterrupt:
# create spi object
# open spi port 0, device (CS) 1
# transfer one byte
# sleep for 0.1 seconds
# Ctrl+C pressed, so...
	spi.close()
