import spidev
import time
import math

class MAX31865(object):

	def __init__(self,port=0, device=0):
		self.spi = spidev.SpiDev()
		self.spi.open(port, device)
		self.connected = 1
		self.spi.max_speed_hz=1000000
		self.spi.mode = 1 #CPHA must be 1 for MAX31865
		self.error = 0
		if self.setRegister(0, 0xD1) < 0:
			print "MAX31865 Init Failed"
			return
		self.autoconversion = 1
		return

	def getRegister(self, reg = -1):
		if reg < 0:
			return -1
		reg = self.spi.xfer2([reg, 0xFF])
		return reg[1]

	def setRegister(self, reg = -1, value = 0):
		if reg < 0:
			return -1
		reg |= 0x80
		return self.spi.xfer2([reg, value])

	def startAutoConversion(self):
		config = self.getRegister(0)
		config |= 0x40
		self.autoconversion = 1
		return self.setRegister(0, config)

	def stopAutoConversion(self):
		config = self.getRegister(0)
		config &= ~0x40
		self.autoconversion = 0
		return self.setRegister(0, config)

	def getTemp(self):
		Rt = self.getResistance()
		if Rt < 50:
			return -1
		#Constants from Callendar-Van Dusen Equation
		A = .0039083
		B = -0.0000005775
		Ro = 100
		T = (-A+math.sqrt(A*A-4*B*(1-(Rt/Ro))))/(2*B)
		return round(T,2)

	def getResistance(self):
		if self.autoconversion != 1:
			config = self.getRegister(0)
			config |= 0x20
			self.setRegister(0, config)
			time.sleep(0.06)
		MSB = self.getRegister(1)
		LSB = self.getRegister(2)
		if LSB%2 == 1:
			return -1
		rawValue = MSB*128 + LSB/2
		ratio = rawValue*0.0000305139
		return ratio*400

	def faultDetect(self):
		oldConfig = self.getRegister(0)
		self.setRegister(0, 0x95)
		time.sleep(0.05)
		if (self.getRegister(0) & 0x0C) != 0:
			self.setRegister(0,oldConfig)
			return -1
		else:
			return self.getRegister(7)

	def faultReset(self):
		config = self.getRegister(0)
		config |= 0x2
		return self.setRegister(0, config)
