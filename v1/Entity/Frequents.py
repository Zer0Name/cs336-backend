import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Frequents(object):
	
	def __init__(self):
		self.bar = None
		self.drinker = None

	def setBar(self, bar):
		self.bar = str(bar)

	def setDrinker(self, drinker):
		self.drinker = str(drinker)

	def getBar(self):
		return str(self.bar)

	def getDrinker(self):
		return str(self.drinker)

	def toJson(self):
		return {
			"bar"  :  self.getBar(),
			"drinker"  :  self.getDrinker()
		}
		
	def map(self, data):
		self.setBar(data["bar"])
		self.setDrinker(date["drinker"])

	def reset(self):
		self.bar = None
		self.drinker = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		bar = str(request.get('bar'))
		drinker = str(request.get('drinker'))
		if variable.isEmpty(bar) or variable.isEmpty(drinker):
			raise MissingParamaters("Missing parameter")
		self.setBar(bar)
		self.setDrinker(drinker)


	def __str__(self):
		return "bar = %s, drinker = %s" % (self.getBar(), self.getDrinker())
