import serial
import time

class pH_probe(object):

	def __init__(self, port='/dev/ttyS0'):
		self.uart = serial.Serial(port = port)
		self.temp = 24.0
		self.error = 0
		self.connected = 1
		return

	### ledon - TRUE or FALSE to enable/disable EZOpH LED ###
	def setLED(self, ledon):
		ledstring = "1" if ledon else "0"
		if self.connected:
			self.uart.write("L," + ledstring + "\r")
			response = self.uart.read(4)
			if response == "*OK\r":
				return 1
			else:
				return -2
		else:
			return -1

	### duration - number of seconds (floats allowed) to flash LED ###
	def find(self, duration = 2):
		if self.connected:
			self.uart.write("Find\r")
			response = self.uart.read(4)
			if response == "*OK\r":
				time.sleep(duration)
				self.uart.write("s") #any character to terminate find mode
				return 1
			else:
				return -2
		else:
			return -1

	def pHRead(self):
		if self.connected:
			self.uart.write("R\r")
			response = self.uart.read(10)
			if response[6:10] == "*OK\r":
				return float(response[0:5])
			else:
				return -2
		else:
			return -1

	calstrings = { 	"mid" : "mid,7.00",
			"low" : "low,4.00",
			"high": "high,10.00"
			}

	### point - calibration point, mid (7.0pH), low (4.0pH), high(10.0pH), or clear ###
	### Issuing a cal-mid will clear all other calibration points ###
	def cal(self, point):
		if point in calstrings:
			paramstring = calstrings[point]
		elif point == "clear":
			paramstring = "clear"
		else:
			return -3
		if self.connected:
			self.uart.write("Cal," + paramstring + "\r")
			response = self.uart.read(4)
			if response == "*OK\r":
				return 1
			else:
				return -2
		else:
			return -1

	### set the internal temperature compensation on the board ###
	def setTempComp(self, temp):
		self.temp = round(temp,1)
		if self.connected:
			self.uart.write("T," + str(self.temp) + "\r")
			response = self.uart.read(4)
			if response == "*OK\r":
				return 1
			else:
				return -2
		else:
			return -1
		return

	def __del__(self):
		if self.connected:
			self.uart.close()
			del self.uart
		return
