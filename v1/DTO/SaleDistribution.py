import random
import time
import datetime

class SaleDistribution(object):
	
	def __init__(self):
		self.total = None
		self.period = None


	def toJson(self):
		return {
			"total" : self.total,
			"period" : self.name 
		}
		
	def map(self, data):
		self.total = str(data["num_bills"])
		self.name = str(data["period"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
