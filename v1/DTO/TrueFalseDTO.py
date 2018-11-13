import random
import time
import datetime

class TrueFalseDTO(object):
	
	def __init__(self):
		self.value = None


	def toJson(self):
		return {
			"value" : self.value
		}
		
	def map(self, data):
		self.value = str(data["value"])
	
	def getValue(self):
		return self.value

	def __str__(self):
		return "value = %s" % (self.getValue())

