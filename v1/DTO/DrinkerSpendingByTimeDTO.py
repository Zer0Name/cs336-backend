import random
import time
import datetime

class DrinkerSpendingByTimeDTO(object):
	
	def __init__(self):
		self.totalPrice = None
		self.period = None


	def toJson(self):
		return {
			"total_price" : self.totalPrice,
			"period" : self.period 
		}
		
	def map(self, data):
		self.totalPrice = str(data["amount_spent"])
		self.period = str(data["period"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
