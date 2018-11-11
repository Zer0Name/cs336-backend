from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.OperatesRepo as OperatesRepo

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
	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.insertOperates(operates)

'''
checks to make:
no duplicate entries
bar exists
day exists
end time is before 24:00
start time is before end time
'''
def updateOperates(operates,oldDay, oldBar):
	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.updateOperates(operates, oldDay, oldBar)

''' 
checks:
past transactions and shifts shouldn't be affected
no bartender works during those hours
'''
def deleteOperates(operates):
	operatesRepo = OperatesRepo.OperatesRepo()
	return operatesRepo.deleteOperates(operates)

def insertOperatesForToday():
    operatesRepo = OperatesRepo.OperatesRepo()
    date =  operatesRepo.getLastInsertedDate()

    operatesRepo = OperatesRepo.OperatesRepo()
    items = operatesRepo.getLastOperates(date)

    operatesRepo = OperatesRepo.OperatesRepo()
    operatesRepo.insertOperatesForToday(items,date)
    return "Success"
