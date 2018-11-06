import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class BarFood(object):
	
	def __init__(self):
		self.name = None

	def setName(self, name):
		self.name = str(name)

	def getName(self):
		return str(self.name)

	def toJson(self):
		return {
			"name"  :  self.getName()
		}
		
	def map(self, data):
		self.setName(data["name"])

	def reset(self):
		self.name = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		name = str(request.get('name'))
		if variable.isEmpty(name):
			raise MissingParamaters("Missing parameter")
		self.setName(name)


	def __str__(self):
		return "name = %s" % (self.getName())
