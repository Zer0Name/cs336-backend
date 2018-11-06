import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Likes(object):
	
	def __init__(self):
		self.beer = None
		self.drinker = None

	def setBeer(self, beer):
		self.beer = str(beer)

	def setDrinker(self, drinker):
		self.drinker = str(drinker)

	def getBeer(self):
		return str(self.beer)

	def getDrinker(self):
		return str(self.drinker)

	def toJson(self):
		return {
			"beer"  :  self.getBeer(),
			"drinker"  :  self.getDrinker()
		}
		
	def map(self, data):
		self.setBeer(data["beer"])
		self.setDrinker(data["drinker"])

	def reset(self):
		self.beer = None
		self.drinker = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		beer = str(request.get('beer'))
		drinker = str(request.get('drinker'))
		if variable.isEmpty(beer) or variable.isEmpty(drinker):
			raise MissingParamaters("Missing parameter")
		self.setBeer(beer)
		self.setDrinker(drinker)


	def __str__(self):
		return "beer = %s, drinker = %s" % (self.getBeer(), self.getDrinker())
