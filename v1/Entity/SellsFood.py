import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class SellsFood(object):
	
	def __init__(self):
		self.foodname = None
		self.barname = None
		self.price = None

	def setFoodname(self, foodname):
		self.foodname = str(foodname)
	
	def setBarname(self, barname):
		self.barname = str(barname)

	def setPrice(self, price):
		self.price = str(price)

	def getFoodname(self):
		return str(self.foodname)
	
	def getBarname(self):
		return str(self.barname)

	def getPrice(self):
		return str(self.price)

	def toJson(self):
		return {
			"foodname"  :  self.getFoodname(),
			"barname"  :  self.getBarname(),
			"price"  :  self.getPrice()
		}
		
	def map(self, data):
		self.setFoodname(data["foodname"])
		self.setBarname(data["barname"])
		self.setPrice(data["price"])

	def reset(self):
		self.foodname = None
		self.barname = None
		self.price = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		foodname = str(request.get('foodname'))
		barname = str(request.get('barname'))
		price = str(request.get('price'))
		if variable.isEmpty(foodname) or variable.isEmpty(barname) or variable.isEmpty(price):
			raise MissingParamaters("Missing parameter")
		self.setFoodname(foodname)
		self.setBarname(barname)
		self.setPrice(price)


	def __str__(self):
		return "foodname = %s, barname = %s, price = %s" % (self.getFoodname(), self.getBarname(), self.getPrice())
