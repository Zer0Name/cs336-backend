import random
import time
import datetime

class DrinkerTransactionDTO(object):
	
	def __init__(self):
		self.bar = None
		self.date = None
		self.time = None
		self.billId = None
		self.item = None
		self.quantity = None
		self.totalItemPrice = None


	def toJson(self):
		return {
			"bar"  :  self.bar,
			"time" :  self.time,
			"bill_id":self.billId ,
			"item" : self.item ,
			"quantity" : self.quantity ,
			"total_item_price" :self.totalItemPrice,
			"date" : self.date
		}
		
	def map(self, data):
		self.bar = str(data["bar"])
		self.date = str(data["date"])
		self.time = str(data["time"])
		self.billId = str(data["bill_id"])
		self.item = str(data["item"])
		self.quantity = str(data["quantity"])
		self.totalItemPrice = str(data["price"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
