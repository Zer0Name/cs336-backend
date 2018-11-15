
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

def getAllShifts(num):
	shiftsRepo = ShiftsRepo.ShiftsRepo() 
	results = shiftsRepo.getAllShifts()
	if len(results) <= num:
		return jsonify([])
	if num+5000 >= len(results):
		return  jsonify([e.toJson() for e in results[num:]])
	else:
		return  jsonify([e.toJson() for e in results[num: num+5000]])
  
def insertShiftsForToday():
	shiftRepo = ShiftsRepo.ShiftsRepo()
	date =  str(shiftRepo.getLastInsertedDate())
	date_N_days_ago = datetime.now()
	if str(str(date_N_days_ago).split()[0]) == str(date):
		return "day already inserted"

	shiftRepo = ShiftsRepo.ShiftsRepo()
	items = shiftRepo.getLastShifts(date)

	datetime_object = datetime.strptime(date, "%Y-%m-%d")
	datetime_object = datetime_object + timedelta(days=1)

	for item in items:
		item.setDate(str(str(datetime_object).split()[0]))
		try:
			shiftRepo = ShiftsRepo.ShiftsRepo()
			shiftRepo.insertShiftsForToday(item)
		except:
			pass
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

	bartenderRepo = BartenderRepo.BartenderRepo()
	bartenderArray = bartenderRepo.getBartender(shifts.getBartender())
	if variable.isEmptyArray(bartenderArray):
		raise Error("Bartender does not exist")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	items = shiftsRepo.getShifts(shifts.getBartender(), shifts.getDate())
	if len(items) != 0:
		raise Error("Bartender can only have one shift on a given date")

	barRepo = BarRepo.BarRepo()
	barArray = barRepo.getBar(shifts.getBar())
	if variable.isEmptyArray(barArray):
		raise Error("Bar does not exist")

	datetime_object = datetime.strptime(shifts.getDate(), "%Y-%m-%d")
	if str(calendar.day_name[datetime_object.weekday()]) != str(shifts.getDay()):
		raise Error("Day does not match date")

	if shifts.getStart() >= shifts.getEnd():
		raise Error("shifts hour error: start time cannot be before end time")

	operatesRepo = OperatesRepo.OperatesRepo()
	if not operatesRepo.shift_during_operating_hours(shifts.getStart(), shifts.getEnd(), shifts.getBar(), shifts.getDate()):
		raise Error("bar does not operate during that shift")

	if barArray[0].getState() != bartenderArray[0].getState():
		raise Error("bartender cannot live in a different state than the bar")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.insertShifts(shifts)

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
	bartenderRepo = BartenderRepo.BartenderRepo()
	bartenderArray = bartenderRepo.getBartender(shifts.getBartender())
	if variable.isEmptyArray(bartenderArray):
		raise Error("Bartender does not exist")

	#pattern 5
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	items = shiftsRepo.getShifts(shifts.getBartender(), shifts.getDate())
	if not variable.isEmpty(items) and (not shifts.getBartender() == oldBartender or not shifts.getBar() == oldBar or not shifts.getDate() == oldDate):
		raise Error("Bartender can only have one shift on a given date")

	barRepo = BarRepo.BarRepo()
	barArray = barRepo.getBar(shifts.getBar())
	if variable.isEmptyArray(barArray):
		raise Error("Bar does not exist")

	datetime_object = datetime.strptime(shifts.getDate(), "%Y-%m-%d")
	if str(calendar.day_name[datetime_object.weekday()]) != str(shifts.getDay()):
		raise Error("Day does not match date")

	if shifts.getStart() >= shifts.getEnd():
		raise Error("shifts hour error: start time cannot be before end time")
		
	operatesRepo = OperatesRepo.OperatesRepo()
	if not operatesRepo.shift_during_operating_hours(shifts.getStart(), shifts.getEnd(), shifts.getBar(), shifts.getDate()):
		raise Error("bar does not operate during that shift")

	if barArray[0].getState() != bartenderArray[0].getState():
		raise Error("bartender cannot live in a different state than the bar")

	billsRepo = BillsRepo.BillsRepo()
	transcations = billsRepo.getBillsByBartenderAndDate(shifts.getBartender(),shifts.getDate())
	if not variable.isEmptyArray(transcations):
		raise Error("Bartender has transcations during the current shift that need to be deleted or updated before trying to update this shift")

	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.updateShifts(shifts, oldBar, oldBartender, oldDate)

''' 
checks:
would need to update transactions? or past transactions stay the same???
can't delete if no other bartender(s) has a shift during that time
'''
def deleteShifts(shifts):
	billsRepo = BillsRepo.BillsRepo()
	transcations = billsRepo.getBillsByBartenderAndDate(shifts.getBartender(),shifts.getDate())
	if not variable.isEmptyArray(transcations):
		raise Error("Bartender has transcations during the shift, please delete them before trying to delete shift")
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.deleteShifts(shifts)
