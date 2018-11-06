import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters
class Beer(object):
	
	def __init__(self):
		self.name = None
		self.manf = None

	def setName(self, name):
		self.name = str(name)

	def setManf(self, manf):
		self.manf = str(manf)

	def getName(self):
		return str(self.name)

	def getManf(self):
		return str(self.manf)

	def toJson(self):
		return {
			"name"  :  self.getName(),
			"manf" :  self.getManf()
		}
		
	def map(self, data):
		self.setName(data["name"])
		self.setManf(data["manf"])

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		name = str(request.get('name'))
		manf = str(request.get('manf'))
		if variable.isEmpty(name) or variable.isEmpty(manf):
			raise MissingParamaters("Missing parameter")
		self.setName(name)
		self.setManf(manf)

		
	def reset(self):
		self.name = None
		self.manf = None

	def __str__(self):
		return "name = %s, manf = %s" % (self.getName(),self.getManf())
