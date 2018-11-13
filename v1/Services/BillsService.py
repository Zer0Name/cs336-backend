from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BillsRepo as BillsRepo
from v1.Exceptions.InvalidInfo import InvalidInfo
from datetime import datetime, timedelta
import calendar

def getAllBills():
	billsRepo = BillsRepo.BillsRepo() 
	results = billsRepo.getAllBills()
	return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
if no corresponding bills items price, tax, and total price must be zero?
if corresponding bills items price = total of those bills
bartender works at the bar
bar exists
bartender exists
drinker exists
bill_id is not in the table yet (unique)
make sure the day corresponds to the date
tax is 7% of the items price
total price is items price + tax + tip
time is during bar's hours and during bartender's shift
'''
def insertBills(bills):
	billsRepo = BillsRepo.BillsRepo()
	if not billsRepo.bar_exists(bills.getBar()):
		raise InvalidInfo("bar does not exist") 
	if not billsRepo.bartender_exists(bills.getBartender()):
		raise InvalidInfo("bartender does not exist") 
	if not billsRepo.drinker_exists(bills.getDrinker()):
		raise InvalidInfo("drinker does not exist") 
	datetime_object = datetime.strptime(bills.getDate(), "%Y-%m-%d")
	if not calendar.day_name[datetime_object.weekday()] == bills.getDay():
		raise InvalidInfo("Day does not match date")
	if billsRepo.duplicate_entry(bills.getBillId()):
		raise InvalidInfo("duplicate entry") 
	if not billsRepo.time_during_shift(bills.getTime(), bills.getBartender(), bills.getBar(), bills.getDate()):
		raise InvalidInfo("Bartender does not have shift at the bar and/or on that date and/or during that time") 
	if not billsRepo.time_during_operating_hours(bills.getTime(), bills.getBar(), bills.getDate()):
		raise InvalidInfo("Bar is not open during that time")
	if not billsRepo.check_items_price(bills.getBillId(), bills.getItemsPrice()):
		raise InvalidInfo("Price of all the items doesn't match the total of the corresponding transactions") 
	if not bills.getTaxPrice() == bills.getItemsPrice()*0.07:
		raise InvalidInfo("Tax is not 7 percent of the items price")
	if not bills.getTaxPrice() + bills.getTip() + bills.getItemsPrice() == bills.getTotalPrice():
		raise InvalidInfo("Incorrect total price")
	
	return billsRepo.insertBills(bills)

'''
checks to make:
no duplicate entries
if no corresponding bills items price, tax, and total price must be zero?
if corresponding bills items price = total of those bills
bartender works at the bar
bar exists
bartender exists
drinker exists
bill_id is not in the table yet (unique)
make sure the day corresponds to the date
tax is 7% of the items price
total price is items price + tax + tip
time is during bar's hours and during bartender's shift
'''
def updateBills(bills,oldBillId):
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.updateBills(bills, oldBillId)

''' 
checks:
would need to update bills and maybe inventory
'''
def deleteBills(bills):
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.deleteBills(bills)