from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BartenderRepo as BartenderRepo

def getAllBartenders():
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getAllBartenders()
    return  jsonify([e.toJson() for e in results])

def getBarsWorkAt(bartender):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getBarsWorkAt(bartender)
    return  jsonify([e.toJson() for e in results])

def getAllPastShifts(bartender,bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getAllPastShifts(bartender,bar)
    return  jsonify([e.toJson() for e in results])

def getNumberOfEachBeerBrandSold(bartender,bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getNumberOfEachBeerBrandSold(bartender,bar)
    return  jsonify([e.toJson() for e in results])

def rankByNumberOfBeersSold(startTime, endTime, day, bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.rankByNumberOfBeersSold(startTime, endTime, day, bar)
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
No bartender can have the same name
check is implemented in table

bartender works in bar in the same state 

Check that no drinker has the same name (and phone number?)
'''
def insertBartender(bartender):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.insertBartender(bartender)

'''
checks to make:
No bartender can have the same name 
check is implemented in table

bartender works in bar in the same state 
Check that no drinker has the same name (and phone number?)
'''
def updateBartender(bartender,oldName):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.updateBartender(bartender,oldName)

''' no check cascade should be handled by table '''
def deleteBartender(bartender):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.deleteBartender(bartender)
    