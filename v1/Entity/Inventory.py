import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Inventory(object):
	
	def __init__(self):
		self.beer = None
		self.bar = None
		self.date = None
		self.startquantity = None
		self.endquantity = None

	def setBeer(self, beer):
		self.beer = str(beer)
	
	def setBar(self, bar):
		self.bar = str(bar)
	
	def setDate(self, date):
		self.date = str(date)

	def setStartQuantity(self, startquantity):
		self.startquantity = str(startquantity)
	
	def setEndQuantity(self, endquantity):
		self.endquantity = str(endquantity)

	def getBeer(self):
		return str(self.beer)
	
	def getBar(self):
		return str(self.bar)
	
	def getDate(self):
		return str(self.date)

	def getStartQuantity(self):
		return str(self.startquantity)
	
	def getEndQuantity(self):
		return str(self.endquantity)

	def toJson(self):
		return {
			"beer"  :  self.getBeer(),
			"bar"  :  self.getBar(),
			"date"  :  self.getDate(),
			"startquantity"  :  self.getStartQuantity(),
			"endquantity"  :  self.getEndQuantity()
		}
		
	def map(self, data):
		self.setBeer(data["beer"])
		self.setBar(data["bar"])
		self.setDate(data["date"])
		self.setStartQuantity(data["startquantity"])
		self.setEndQuantity(data["endquantity"])

	def reset(self):
		self.beer = None
		self.bar = None
		self.date = None
		self.startquantity = None
		self.endquantity = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		beer = str(request.get('beer'))
		bar = str(request.get('bar'))
		date = str(request.get('date'))
		startquantity = str(request.get('startquantity'))
		endquantity = str(request.get('endquantity'))
		if variable.isEmpty(beer) or variable.isEmpty(bar) or variable.isEmpty(date) or variable.isEmpty(startquantity) or variable.isEmpty(endquantity):
			raise MissingParamaters("Missing parameter")
		self.setBeer(beer)
		self.setBar(bar)
		self.setDate(date)
		self.setStartQuantity(startquantity)
		self.setEndQuantity(endquantity)


	def __str__(self):
		return "beer = %s, bar = %s , date = %s, startquantity = %s, endquantity = %s" % (self.getBeer(), self.getBar(), self.getDate(), self.getStartQuantity(), self.getEndQuantity())
