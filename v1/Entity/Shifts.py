import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Shifts(object):
	
	def __init__(self):
		self.bar = None
		self.day = None
		self.bartender = None
		self.start = None
		self.end = None
	
	def setBar(self, bar):
		self.bar = str(bar)
	
	def setBartender(self, bartender):
		self.bartender = str(bartender)
	
	def setDay(self, day):
		self.day = str(day)

	def setStart(self, start):
		self.start = str(start)
	
	def setEnd(self, end):
		self.end = str(end)
	
	def getBar(self):
		return str(self.bar)

	def getBartender(self):
		return str(self.bartender)
	
	def getDay(self):
		return str(self.day)

	def getStart(self):
		return str(self.start)
	
	def getEnd(self):
		return str(self.end)

	def toJson(self):
		return {
			"bar"  :  self.getBar(),
			"bartender"  :  self.getBartender(),
			"day"  :  self.getDay(),
			"start"  :  self.getStart(),
			"end"  :  self.getEnd()
		}
		
	def map(self, data):
		self.setBar(data["bar"])
		self.setBartender(data["bartender"])
		self.setDay(data["day"])
		self.setStart(data["start"])
		self.setEnd(data["end"])

	def reset(self):
		self.bar = None
		self.bartender = None
		self.day = None
		self.start = None
		self.end = None

	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		bar = str(request.get('bar'))
		bartender = str(request.get('bartender'))
		day = str(request.get('day'))
		start = str(request.get('start'))
		end = str(request.get('end'))
		if variable.isEmpty(bar) or variable.isEmpty(bartender) or variable.isEmpty(day) or variable.isEmpty(start) or variable.isEmpty(end):
			raise MissingParamaters("Missing parameter")
		self.setBar(bar)
		self.setBartender(bartender)
		self.setDay(day)
		self.setStart(start)
		self.setEnd(end)


	def __str__(self):
		return "bar = %s, bartender = %s , day = %s, start = %s, end = %s" % (self.getBar(), self.getBartender(), self.getDay(), self.getStart(), self.getEnd())
