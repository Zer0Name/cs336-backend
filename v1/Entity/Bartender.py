import random
import time
import datetime

import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Bartender(object):
	
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

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		name = str(request.get('name'))
		phone = str(request.get('phone'))
		state = str(request.get('state'))
		if variable.isEmpty(name) or variable.isEmpty(phone) or variable.isEmpty(state):
			raise MissingParamaters("Missing parameter")
		self.setName(name)
		self.setPhone(phone)
		self.setState(state)


	def __str__(self):
		return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
