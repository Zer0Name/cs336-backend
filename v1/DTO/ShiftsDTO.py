import random
import time
import datetime

class ShiftsDTO(object):
	
	def __init__(self):
		self.day = None
		self.start = None
		self.end = None


	def toJson(self):
		return {
			"day" : self.day,
			"start" : self.start,
			"end" : self.end 
		}
		
	def map(self, data):
		self.day = str(data["day"])
		self.start = str(data["start"])
		self.end = str(data["end"])

