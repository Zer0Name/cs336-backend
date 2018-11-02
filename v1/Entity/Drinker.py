import random
import time
import datetime
class Drinker(object):
	
	def __init__(self):
		self.name = None
		self.phone = None
		self.state = None

	def setName(self, name):
		self.name = str(name)

	def setPhone(self, phone):
		self.phone = str(phone)

	def setState(self, state):
		self.state = str(state)

	def getName(self):
		return str(self.name)

	def getPhone(self):
		return str(self.phone)

	def getState(self):
		return str(self.state)

	def toJson(self):
		return {
			"name"  :  self.getName(),
			"phone" :  self.getPhone(),
			"state" :  self.getState()
		}
		
	def map(self, data):
		self.setName(data["name"])
		self.setPhone(data["phone"])
		self.setState(data["state"])

	def reset(self):
		self.name = None
		self.phone = None
		self.state = None



	def __str__(self):
		return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
