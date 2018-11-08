import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters
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

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		name = str(request.get('name'))
		state = str(request.get('state'))
		if variable.isEmpty(name) or variable.isEmpty(state):
			raise MissingParamaters("Missing parameter")
		self.setName(name)
		self.setState(state)

	def reset(self):
		self.name = None
		self.state = None

	def __str__(self):
		return "name = %s, state = %s" % (self.getName(),self.getState())
