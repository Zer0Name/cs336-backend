import random
import time
import datetime

class NameDTO(object):
	
	def __init__(self):
		self.name = None


	def toJson(self):
		return {
			"name" : self.name
		}
		
	def map(self, data):
		self.name = str(data["name"])

