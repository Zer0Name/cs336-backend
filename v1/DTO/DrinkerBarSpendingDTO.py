import random
import time
import datetime

class DrinkerBarSpendingDTO(object):
	
	def __init__(self):
		self.totalPrice = None
		self.period = None
		self.bar = None


	def toJson(self):
		return {
			"period" : self.period,
			"total_price" : self.totalPrice,
			"bar" : self.bar 
		}
		
	def map(self, data):
		self.totalPrice = str(data["amount_spent"])
		self.period = str(data["period"])
		self.bar = str(data["bar"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
