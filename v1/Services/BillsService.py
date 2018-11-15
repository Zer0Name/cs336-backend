from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BillsRepo as BillsRepo
import v1.Repos.BarRepo as BarRepo
import v1.Repos.DrinkersRepo as DrinkersRepo
import v1.Repos.BartenderRepo as BartenderRepo
import v1.Repos.OperatesRepo as OperatesRepo
import v1.Repos.ShiftsRepo as ShiftsRepo
import v1.Repos.TransactionsRepo as TransactionsRepo

from v1.Exceptions.Error import Error
from datetime import datetime, timedelta
import calendar

def getAllBills(num):
	billsRepo = BillsRepo.BillsRepo() 
	results = billsRepo.getAllBills()
	if len(results) <= num:
		return jsonify([])
	if num+5000 >= len(results):
		return  jsonify([e.toJson() for e in results[num:]])
	else:
		return  jsonify([e.toJson() for e in results[num: num+5000]])

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
make sur e the day corresponds to the date
tax is 7% of the items price
total price is items price + tax + tip
time is during bar's hours and during bartender's shift
'''
def insertBills(bills):

	barRepo = BarRepo.BarRepo()
	if not barRepo.bar_exists(bills.getBar()):
		raise Error("bar does not exist") 

	bartenderRepo = BartenderRepo.BartenderRepo()
	if not bartenderRepo.bartender_exists(bills.getBartender()):
		raise Error("bartender does not exist") 

	drinkerRepo = DrinkersRepo.DrinkersRepo()
	if not drinkerRepo.drinker_exists(bills.getDrinker()):
		raise Error("drinker does not exist") 

	datetime_object = datetime.strptime(bills.getDate(), "%Y-%m-%d")
	if not calendar.day_name[datetime_object.weekday()] == bills.getDay():
		raise Error("Day does not match date")

	billsRepo = BillsRepo.BillsRepo()
	if billsRepo.duplicate_entry(bills.getBillId()) and not(bills.getBillId() == oldBillId):
		raise Error("duplicate entry") 

	operatesRepo = OperatesRepo.OperatesRepo() 
	if not operatesRepo.time_during_operating_hours(bills.getTime(), bills.getBar(), bills.getDate()):
		raise Error("Bar is not open during that time")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	if not shiftsRepo.time_during_shift(bills.getTime(), bills.getBartender(), bills.getBar(), bills.getDate()):
		raise Error("Bartender does not have shift at the bar and/or on that date and/or during that time")

	# if not float(bills.getTaxPrice()) == round(float(bills.getItemsPrice())*0.07,2):
	# 	raise Error("Tax is not 7 percent of the items price")

	# if not float(bills.getTaxPrice()) + float(bills.getTip()) + float(bills.getItemsPrice()) == float(bills.getTotalPrice()):
	# 	raise Error("Incorrect total price")
	
	# billsRepo = BillsRepo.BillsRepo()
	# if not billsRepo.check_items_price(bills.getBillId(), bills.getItemsPrice()):
	# 	raise Error("Price of all the items doesn't match the total of the corresponding transactions") 

	# bills.setTaxPrice(0)
	# bills.setItemsPrice(0)
	# bills.setTip(0)
	# bills.setTotalPrice(0)
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.insertBills(bills)

def updateBills(bills,oldBillId):

	barRepo = BarRepo.BarRepo()
	if not barRepo.bar_exists(bills.getBar()):
		raise Error("bar does not exist") 

	bartenderRepo = BartenderRepo.BartenderRepo()
	if not bartenderRepo.bartender_exists(bills.getBartender()):
		raise Error("bartender does not exist") 

	drinkerRepo = DrinkersRepo.DrinkersRepo()
	if not drinkerRepo.drinker_exists(bills.getDrinker()):
		raise Error("drinker does not exist")

	billsRepo = BillsRepo.BillsRepo()
	if billsRepo.duplicate_entry(bills.getBillId()) and not(bills.getBillId() == oldBillId):
		raise Error("duplicate entry")  

	datetime_object = datetime.strptime(bills.getDate(), "%Y-%m-%d")
	if not calendar.day_name[datetime_object.weekday()] == bills.getDay():
		raise Error("Day does not match date")

	operatesRepo = OperatesRepo.OperatesRepo() 
	if not operatesRepo.time_during_operating_hours(bills.getTime(), bills.getBar(), bills.getDate()):
		raise Error("Bar is not open during that time")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	if not shiftsRepo.time_during_shift(bills.getTime(), bills.getBartender(), bills.getBar(), bills.getDate()):
		raise Error("Bartender does not have shift at the bar and/or on that date and/or during that time")

	# if not float(bills.getTaxPrice()) == round(float(bills.getItemsPrice())*0.07,2):
	# 	raise Error("Tax is not 7 percent of the items price")

	# if not float(bills.getTaxPrice()) + float(bills.getTip()) + float(bills.getItemsPrice()) == float(bills.getTotalPrice()):
	# 	raise Error("Incorrect total price")
	
	# billsRepo = BillsRepo.BillsRepo()
	# if not billsRepo.check_items_price(bills.getBillId(), bills.getItemsPrice()):
	# 	raise Error("Price of all the items doesn't match the total of the corresponding transactions")
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.updateBills(bills, oldBillId)

''' 
checks:
would need to update bills and maybe inventory
'''
def deleteBills(bills):
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	results = transactionsRepo.getAllTransactionsForBillId(bills.getBillId())
	for r in results:
		transactionsRepo = TransactionsRepo.TransactionsRepo()
		transactionsRepo.deleteTransactions(r)
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.deleteBills(bills)