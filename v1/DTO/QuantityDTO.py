import random
import time
import datetime

class QuantityDTO(object):
	
	def __init__(self):
		self.total = None
		self.name = None


	def toJson(self):
		return {
			"total" : self.total,
			"name" : self.name 
		}
		
	def map(self, data):
		self.total = str(data["amount"])
		self.name = str(data["name"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
