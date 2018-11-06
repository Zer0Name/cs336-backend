import random
import time
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

class Bills(object):
	
	def __init__(self):
		self.bill_id = None
		self.bar = None
		self.date = None
		self.drinker = None
		self.items_price = None
		self.tax_price = None
		self.tip = None
		self.total_price = None
		self.time = None
		self.bartender = None
		self.day = None

	def setBillId(self, bill_id):
		self.bill_id = str(bill_id)

	def setBar(self, bar):
		self.bar = str(bar)

	def setDate(self, date):
		self.date = str(date)
	
	def setDrinker(self, drinker):
		self.drinker = str(drinker)
	
	def setItemsPrice(self, items_price):
		self.items_price = str(items_price)
	
	def setTaxPrice(self, tax_price):
		self.tax_price = str(tax_price)

	def setTip(self, tip):
		self.tip = str(tip)
	
	def setTotalPrice(self, total_price):
		self.total_price = str(total_price)
	
	def setTime(self, time):
		self.time = str(time)
	
	def setBartender(self, bartender):
		self.bartender = str(bartender)
	
	def setDay(self, day):
		self.day = str(day)

	def getBillId(self):
		return str(self.bill_id)

	def getBar(self):
		return str(self.bar)

	def getDate(self):
		return str(self.date)
	
	def getDrinker(self):
		return str(self.drinker)
	
	def getItemsPrice(self):
		return str(self.items_price)
	
	def getTaxPrice(self):
		return str(self.tax_price)

	def getTip(self):
		return str(self.tip)
	
	def getTotalPrice(self):
		return str(self.total_price)
	
	def getTime(self):
		return str(self.time)
	
	def getBartender(self):
		return str(self.bartender)
	
	def getDay(self):
		return str(self.day)

	def toJson(self):
		return {
			"bill_id"  :  self.getBillId(),
			"bar" :  self.getBar(),
			"date" :  self.getDate(),
			"drinker" :  self.getDrinker(),
			"items_price" :  self.getItemsPrice(),
			"tax_price" :  self.getTaxPrice(),
			"tip" :  self.getTip(),
			"total_price" :  self.getTotalPrice(),
			"time" :  self.getTime(),
			"bartender" :  self.getBartender(),
			"day" :  self.getDay()
		}
		
	def map(self, data):
		self.setBillId(data["bill_id"])
		self.setBar(data["bar"])
		self.setDate(data["date"])
		self.setDrinker(data["drinker"])
		self.setItemsPrice(data["items_price"])
		self.setTaxPrice(data["tax_price"])
		self.setTip(data["tip"])
		self.setTotalPrice(data["total_price"])
		self.setTime(data["time"])
		self.setBartender(data["bartender"])
		self.setDay(data["day"])

	def reset(self):
		self.bill_id = None
		self.bar = None
		self.date = None
		self.drinker = None
		self.items_price = None
		self.tax_price = None
		self.tip = None
		self.total_price = None
		self.time = None
		self.bartender = None
		self.day = None


	def requestMap(self,request):
		if variable.isEmpty(request):
			return "Error"
		bill_id = str(request.get('bill_id'))
		bar = str(request.get('bar'))
		date = str(request.get('date'))
		drinker = str(request.get('drinker'))
		items_price = str(request.get('items_price'))
		tax_price = str(request.get('tax_price'))
		tip = str(request.get('tip'))
		total_price = str(request.get('total_price'))
		time = str(request.get('time'))
		bartender = str(request.get('bartender'))
		day = str(request.get('day'))
		if variable.isEmpty(bill_id) or variable.isEmpty(bar) or variable.isEmpty(date) or variable.isEmpty(drinker) or variable.isEmpty(items_price) or variable.isEmpty(tax_price) or variable.isEmpty(tip) or variable.isEmpty(total_price) or variable.isEmpty(time) or variable.isEmpty(bartender) or variable.isEmpty(day):
			raise MissingParamaters("Missing parameter")
		self.setBillId(bill_id)
		self.setBar(bar)
		self.setDate(date)
		self.setDrinker(drinker)
		self.setItemsPrice(items_price)
		self.setTaxPrice(tax_price)
		self.setTip(tip)
		self.setTotalPrice(total_price)
		self.setTime(time)
		self.setBartender(bartender)
		self.setDay(day)

	def __str__(self):
		return "bill_id = %s , bar = %s, date = %s, drinker = %s, items_price = %s, tax_price = %s, tip = %s, total_price = %s, time = %s, bartender = %s, day = %s" % (self.getBillId(), self.getBar(), self.getDate(), self.getDrinker(), self.getItemsPrice(), self.getTaxPrice(), self.getTip(), self.getTotalPrice(), self.getTime(), self.getBartender(), self.getDay())
