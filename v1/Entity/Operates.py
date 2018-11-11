import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Operates(object):
	
	def __init__(self):
		self.bar = None
		self.day = None
		self.start = None
		self.end = None
		self.date = None
	
	def setBar(self, bar):
		self.bar = str(bar)
	
	def setDay(self, day):
		self.day = str(day)

	def setStart(self, start):
		self.start = str(start)
	
	def setEnd(self, end):
		self.end = str(end)

	def setDate(self,date):
		self.date = str(date)
	
	def getBar(self):
		return str(self.bar)
	
	def getDay(self):
		return str(self.day)

	def getStart(self):
		return str(self.start)
	
	def getEnd(self):
		return str(self.end)
	
	def getDate(self):
		return str(self.date)

	def toJson(self):
		return {
			"bar"  :  self.getBar(),
			"day"  :  self.getDay(),
			"start"  :  self.getStart(),
			"end"  :  self.getEnd(),
			"date" : self.getDate()
		}
		
	def map(self, data):
		self.setBar(data["bar"])
		self.setDay(data["day"])
		self.setStart(data["start"])
		self.setEnd(data["end"])
		self.setDate(data["date"])

	def reset(self):
		self.bar = None
		self.day = None
		self.start = None
		self.end = None
		self.date = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		bar = str(request.get('bar'))
		day = str(request.get('day'))
		start = str(request.get('start'))
		end = str(request.get('end'))
		date = str(request.get('date'))
		if variable.isEmpty(bar) or variable.isEmpty(day) or variable.isEmpty(start) or variable.isEmpty(end) or variable.isEmpty(date):
			raise MissingParamaters("Missing parameter")
		self.setBar(bar)
		self.setDay(day)
		self.setStart(start)
		self.setEnd(end)
		self.setDate(date)


	def __str__(self):
		return "bar = %s , day = %s, start = %s, end = %s, date = %s" % (self.getBar(), self.getDay(), self.getStart(), self.getEnd(), self.getDate())
