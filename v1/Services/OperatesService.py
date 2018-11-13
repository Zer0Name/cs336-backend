from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.OperatesRepo as OperatesRepo
import v1.Repos.BarRepo as BarRepo
import v1.Repos.DayRepo as DayRepo
import v1.Repos.ShiftsRepo as ShiftsRepo
import v1.Repos.BillsRepo as BillsRepo
from v1.Exceptions.Error import Error
from datetime import datetime, timedelta
import calendar

def getAllOperates():
	operatesRepo = OperatesRepo.OperatesRepo() 
	results = operatesRepo.getAllOperates()
	return  jsonify([e.toJson() for e in results])

def getOperatesForBar(bar):
	operatesRepo = OperatesRepo.OperatesRepo() 
	results = operatesRepo.getOperatesForBar(bar)
	return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
bar exists
day exists
end time is before 24:00
start time is before end time
'''
def insertOperates(operates):
	barRepo = BarRepo.BarRepo()
	if not barRepo.bar_exists(operates.getBar()):
		raise Error("bar does not exist")
		
	dayRepo = DayRepo.DayRepo()
	if not dayRepo.day_exists(operates.getDay()):
		raise Error("day does not exist")
	
	operatesRepo = OperatesRepo.OperatesRepo()
	if operatesRepo.duplicate_entry(operates.getBar(), operates.getDate()):
		raise Error("Duplicate Entry")

	if not (operates.getEnd() <= "24:00" and operates.getStart() < operates.getEnd()):
		raise Error("Invalid hours provided")

	datetime_object = datetime.strptime(operates.getDate(), "%Y-%m-%d")
	if not calendar.day_name[datetime_object.weekday()] == operates.getDay():
		raise Error("Day does not match date")

	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.insertOperates(operates)


def updateOperates(operates,oldDate, oldBar):
	barRepo = BarRepo.BarRepo()
	if not barRepo.bar_exists(operates.getBar()):
		raise Error("bar does not exist")
		
	dayRepo = DayRepo.DayRepo()
	if not dayRepo.day_exists(operates.getDay()):
		raise Error("day does not exist")
	
	operatesRepo = OperatesRepo.OperatesRepo()
	if operatesRepo.duplicate_entry(operates.getBar(), operates.getDate()) and (not operates.getBar() == oldBar or not operates.getOldDate() == oldDate):
		raise Error("Duplicate Entry")

	if not (operates.getEnd() <= "24:00" and operates.getStart() < operates.getEnd()):
		raise Error("Invalid hours provided")

	datetime_object = datetime.strptime(operates.getDate(), "%Y-%m-%d")
	if not calendar.day_name[datetime_object.weekday()] == operates.getDay():
		raise Error("Day does not match date")

	#check if any bartenders at that bar on that date have shifts when bar is not open
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	shifts = shiftsRepo.getShiftsForBar(operates.getBar(), operates.getDate())
	for s in shifts:
		if s.getStart() < operates.getStart() or s.getEnd() > operates.getEnd():
			raise Error("Update would result in bartender(s) having shift when bar is closed. Please update Shifts table first.")
	#check if any bills at that bar on that date have a time when bar is not open
	billsRepo = BillsRepo.BillsRepo()
	bills = billsRepo.getBillsByBarAndDate(operates.getBar(), operates.getDate())
	for b in bills:
		if b.getTime() < operates.getStart() or b.getTime() > operates.getEnd():
			raise Error("Update would result in bill(s) would result in a time stamp when bar is closed. Please update Bills table first.")
	
	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.updateOperates(operates, oldDate, oldBar)

''' 
checks:
past transactions and shifts shouldn't be affected
no bartender works during those hours
'''
def deleteOperates(operates):
	#check if any bartenders at that bar on that date have shifts when bar is not open
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	shifts = shiftsRepo.getShiftsForBar(operates.getBar(), operates.getDate())
	for s in shifts:
		if s.getStart() < operates.getStart() or s.getEnd() > operates.getEnd():
			raise Error("Deleting these operating hours would result in bartender(s) having shift when bar is closed. Please update Shifts table first.")
	
	#check if any bills at that bar on that date have a time when bar is not open
	billsRepo = BillsRepo.BillsRepo()
	bills = billsRepo.getBillsByBarAndDate(operates.getBar(), operates.getDate())
	for b in bills:
		if b.getTime() < operates.getStart() or b.getTime() > operates.getEnd():
			raise Error("Deleting these operating hours in bill(s) would result in a time stamp when bar is closed. Please update Bills table first.")
	

	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.deleteOperates(operates)

def insertOperatesForToday():
	operatesRepo = OperatesRepo.OperatesRepo()
	date =  str(operatesRepo.getLastInsertedDate())

	operatesRepo = OperatesRepo.OperatesRepo()
	items = operatesRepo.getLastOperates(date)

	operatesRepo = OperatesRepo.OperatesRepo()
	operatesRepo.insertOperatesForToday(items,date)
	return "Success"
