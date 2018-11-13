
import v1.Repos.ShiftsRepo as ShiftsRepo
from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.ShiftsRepo as ShiftsRepo
import v1.Repos.BarRepo as BarRepo
import v1.Repos.BartenderRepo as BartenderRepo
import v1.Repos.OperatesRepo as OperatesRepo
import v1.Repos.BillsRepo as BillsRepo
from v1.Exceptions.Error import Error
import v1.Util.Variable as variable
from datetime import datetime, timedelta
import calendar

def getAllShifts():
	shiftsRepo = ShiftsRepo.ShiftsRepo() 
	results = shiftsRepo.getAllShifts()
	return  jsonify([e.toJson() for e in results])
  
def insertShiftsForToday():
	shiftRepo = ShiftsRepo.ShiftsRepo()
	date =  str(shiftRepo.getLastInsertedDate())

	shiftRepo = ShiftsRepo.ShiftsRepo()
	items = shiftRepo.getLastShifts(date)

	shiftRepo = ShiftsRepo.ShiftsRepo()
	shiftRepo.insertShiftsForToday(items,date)
	return "Success"

'''
checks to make:
no duplicate entries
bar exists
bartender exists
day matches date
start time is after the bar opens
end time is before the bar closes 
'''
def insertShifts(shifts):

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	items = shiftsRepo.getShifts(shifts.getBartender(), shifts.getDate())
	if not variable.isEmpty(items):
		raise Error("Duplicate entry")

	barRepo = BarRepo.BarRepo()
	barArray = barRepo.getBar(shifts.getBar())
	if variable.isEmptyArray(barArray):
		raise Error("Bar does not exist")

	bartenderRepo = BartenderRepo.BartenderRepo()
	bartenderArray = bartenderRepo.getBartender(shifts.getBartender())
	if variable.isEmptyArray(bartenderArray):
		raise Error("Bartender does not exist")

	datetime_object = datetime.strptime(shifts.getDate(), "%Y-%m-%d")
	if str(calendar.day_name[datetime_object.weekday()]) != str(shifts.getDay()):
		raise Error("Day does not match date")

	operatesRepo = OperatesRepo.OperatesRepo()
	items = operatesRepo.getOperatesForBar(shifts.getBar())
	operate = None
	for item in items:
		if item.getDate() == shifts.getDate():
			operate = item
			break
	
	if variable.isEmpty(operate):
		raise Error("bar does not operate on that day")

	if operate.getStart() < shifts.getStart() or operate.getEnd() > shifts.getEnd():
		raise Error("bar is closed during bartenders shift")

	if shifts.getStart() >= operate.getEnd():
		raise Error("shifts hour error start time cant be before end time")

	if barArray[0].getState() != bartenderArray[0].getState():
		raise Error("bartender cant live in a different state than the bar")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	# return shiftsRepo.insertShifts(shifts)
	return "a"

'''
checks to make:
no duplicate entries
bar exists
bartender exists
day matches date
start time is after the bar opens
end time is before the bar closes 
'''
def updateShifts(shifts,oldBar, oldBartender, oldDate):
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	items = shiftsRepo.getShifts(shifts.getBartender(), shifts.getDate())
	if not variable.isEmpty(items):
		raise Error("Duplicate entry")

	barRepo = BarRepo.BarRepo()
	barArray = barRepo.getBar(shifts.getBar())
	if variable.isEmptyArray(barArray):
		raise Error("Bar does not exist")

	bartenderRepo = BartenderRepo.BartenderRepo()
	bartenderArray = bartenderRepo.getBartender(shifts.getBartender())
	if variable.isEmptyArray(bartenderArray):
		raise Error("Bartender does not exist")

	datetime_object = datetime.strptime(shifts.getDate(), "%Y-%m-%d")
	if str(calendar.day_name[datetime_object.weekday()]) != str(shifts.getDay()):
		raise Error("Day does not match date")

	operatesRepo = OperatesRepo.OperatesRepo()
	items = operatesRepo.getOperatesForBar(shifts.getBar())
	operate = None
	for item in items:
		if item.getDate() == shifts.getDate():
			operate = item
			break
	
	if variable.isEmpty(operate):
		raise Error("bar does not operate on that day")

	if operate.getStart() < shifts.getStart() or operate.getEnd() > shifts.getEnd():
		raise Error("bar is closed during bartenders shift")

	if shifts.getStart() >= operate.getEnd():
		raise Error("shifts hour error start time cant be before end time")

	if barArray[0].getState() != bartenderArray[0].getState():
		raise Error("bartender cant live in a different state than the bar")


	shiftsRepo = ShiftsRepo.ShiftsRepo()
	# return shiftsRepo.updateShifts(shifts, oldBar, oldBartender, oldDate)
	return "a"

''' 
checks:
would need to update transactions? or past transactions stay the same???
can't delete if no other bartender(s) has a shift during that time
'''
def deleteShifts(shifts):
	billsRepo = BillsRepo.BillsRepo()
	transcations = billsRepo.getBillsByBartenderAndDate(shifts.getBartender(),shifts.getDate())
	if not variable.isEmptyArray(transcations):
		raise Error("Bartender has transcation during the shift, please delete them before trying to delete shift")
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.deleteShifts(shifts)
