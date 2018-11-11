
import v1.Repos.ShiftsRepo as ShiftsRepo
from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.ShiftsRepo as ShiftsRepo

 
   
def insertShiftsForToday():
    shiftRepo = ShiftsRepo.ShiftsRepo()
    date =  shiftRepo.getLastInsertedDate()

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
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.updateShifts(shifts, oldBar, oldBartender, oldDate)

''' 
checks:
would need to update transactions? or past transactions stay the same???
can't delete if no other bartender(s) has a shift during that time
'''
def deleteShifts(shifts):
	shiftsRepo = ShiftsRepo.ShiftsRepo()
	return shiftsRepo.deleteShifts(shifts)
