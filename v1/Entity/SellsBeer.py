import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class SellsBeer(object):
	
	def __init__(self):
		self.beername = None
		self.barname = None
		self.price = None

	def setBeername(self, beername):
		self.beername = str(beername)
	
	def setBarname(self, barname):
		self.barname = str(barname)

	def setPrice(self, price):
		self.price = str(price)

	def getBeername(self):
		return str(self.beername)
	
	def getBarname(self):
		return str(self.barname)

	def getPrice(self):
		return str(self.price)

	def toJson(self):
		return {
			"beername"  :  self.getBeername(),
			"barname"  :  self.getBarname(),
			"price"  :  self.getPrice()
		}
		
	def map(self, data):
		self.setBeername(data["beername"])
		self.setBarname(data["barname"])
		self.setPrice(data["price"])

	def reset(self):
		self.beername = None
		self.barname = None
		self.price = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		print request
		beername = str(request.get('beername'))
		barname = str(request.get('barname'))
		price = str(request.get('price'))
		if variable.isEmpty(beername) or variable.isEmpty(barname) or variable.isEmpty(price):
			raise MissingParamaters("Missing parameter")
		self.setBeername(beername)
		self.setBarname(barname)
		self.setPrice(price)


	def __str__(self):
		return "beername = %s, barname = %s, price = %s" % (self.getBeername(), self.getBarname(), self.getPrice())
