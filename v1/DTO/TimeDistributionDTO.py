import random
import time
import datetime

class TimeDistributionDTO(object):
	
	def __init__(self):
		self.morning_avg_sold = None
		self.afternoon_avg_sold = None
		self.evening_avg_sold = None
		self.night_avg_sold = None


	def toJson(self):
		return {
			"morning_avg_sold" : self.morning_avg_sold,
			"afternoon_avg_sold" : self.afternoon_avg_sold, 
			"evening_avg_sold" : self.evening_avg_sold, 
			"night_avg_sold" : self.night_avg_sold 
		}
		
	def map(self, data):
		self.morning_avg_sold = str(data["morning_avg_sold"])
		self.afternoon_avg_sold = str(data["afternoon_avg_sold"])
		self.evening_avg_sold = str(data["evening_avg_sold"])
		self.night_avg_sold = str(data["night_avg_sold"])

	# def __str__(self):
	# 	return "name = %s, phone = %s, state = %s" % (self.getName(),self.getPhone(),self.getState() )
