import random
import time
import datetime

class BarTopBeerBrandDTO(object):
	
	def __init__(self):
		self.manf = None
		self.quantity = None


	def toJson(self):
		return {
			"manf" : self.manf,
			"quantity" : self.quantity 
		}
		
	def map(self, data):
		self.manf = str(data["manf"])
		self.quantity = str(data["quantity"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
