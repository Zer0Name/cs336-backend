import random
import time
import datetime

class DrinkerTopBeerDTO(object):
	
	def __init__(self):
		self.beer = None
		self.quantity = None


	def toJson(self):
		return {
			"beer" : self.beer,
			"quantity" : self.quantity 
		}
		
	def map(self, data):
		self.beer = str(data["beer"])
		self.quantity = str(data["quantity"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
