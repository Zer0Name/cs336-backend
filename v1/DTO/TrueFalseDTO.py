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

