import random
import time
import datetime
class Bar(object):
	
	def __init__(self):
		self.name = None
		self.state = None

	def setName(self, name):
		self.name = str(name)

	def setState(self, state):
		self.state = str(state)

	def getName(self):
		return str(self.name)

	def getState(self):
		return str(self.state)

	def toJson(self):
		return {
			"name"  :  self.getName(),
			"state" :  self.getState()
		}
		
	def map(self, data):
		self.setName(data["name"])
		self.setState(data["state"])

	def reset(self):
		self.name = None
		self.state = None

	def __str__(self):
		return "name = %s, state = %s" % (self.getName(),self.getState())
