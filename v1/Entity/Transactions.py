import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Transactions(object):
	
	def __init__(self):
		self.bill_id = None
		self.quantity = None
		self.item = None
		self.type = None
		self.price = None

	def setBillId(self, bill_id):
		self.bill_id = str(bill_id)
	
	def setQuantity(self, quantity):
		self.quantity = str(quantity)
	
	def setItem(self, item):
		self.item = str(item)

	def setType(self, item_type):
		self.type = str(item_type)
	
	def setPrice(self, price):
		self.price = str(price)

	def getBillId(self):
		return str(self.bill_id)
	
	def getQuantity(self):
		return str(self.quantity)
	
	def getItem(self):
		return str(self.item)

	def getType(self):
		return str(self.type)
	
	def getPrice(self):
		return str(self.price)

	def toJson(self):
		return {
			"bill_id"  :  self.getBillId(),
			"quantity" :  self.getQuantity(),
			"item" :  self.getItem(),
			"type" :  self.getType(),
			"price" :  self.getPrice()
		}
		
	def map(self, data):
		self.setBillId(data["bill_id"])
		self.setQuantity(data["quantity"])
		self.setItem(data["item"])
		self.setType(data["type"])
		self.setPrice(data["price"])

	def reset(self):
		self.bill_id = None
		self.quantity = None
		self.item = None
		self.type = None
		self.price = None


	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		bill_id = str(request.get('bill_id'))
		quantity = str(request.get('quantity'))
		item = str(request.get('item'))
		item_type = str(request.get('item_type'))
		price = str(request.get('price'))
		if variable.isEmpty(bill_id) or variable.isEmpty(quantity) or variable.isEmpty(item) or variable.isEmpty(item_type) or variable.isEmpty(price):
			raise MissingParamaters("Missing parameter")
		self.setBillId(bill_id)
		self.setQuantity(quantity)
		self.setItem(item)
		self.setType(item_type)
		self.setPrice(price)
	
	def __str__(self):
		return "bill_id = %s , quantity = %s, item = %s, type = %s, price = %s" % (self.getBillId(), self.getQuantity(), self.getItem(), self.getType(), self.getPrice())

