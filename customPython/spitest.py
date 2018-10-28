#!/usr/bin/python
import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
print spi.bits_per_word
print spi.max_speed_hz
spi.max_speed_hz = 500000
try:
    while True:
	spi.writebytes([0xAA])
#        resp = spi.xfer([0xAA])
        time.sleep(0.1)
    #end while
except KeyboardInterrupt:
# create spi object
# open spi port 0, device (CS) 1
# transfer one byte
# sleep for 0.1 seconds
# Ctrl+C pressed, so...
	spi.close()
