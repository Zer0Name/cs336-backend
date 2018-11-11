from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.DayRepo as DayRepo

def getAllDay():
    dayRepo = DayRepo.DayRepo() 
    results = dayRepo.getAllDay()
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
No day can have the same name
check is implemented in table
NOT SURE ABOUT THIS
'''
def insertDay(day):
	dayRepo = DayRepo.DayRepo()
	return dayRepo.insertDay(day)

'''
checks to make:
No day can have the same name
check is implemented in table
NOT SURE ABOUT THIS
'''
def updateDay(day,oldName):
	dayRepo = DayRepo.DayRepo()
	return dayRepo.updateDay(day,oldName)

''' no check cascade should be handled by table '''
def deleteDay(day):
	dayRepo = DayRepo.DayRepo()
	return dayRepo.deleteDay(day)
