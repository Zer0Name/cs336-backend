from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BarRepo as BarRepo


def getAllBars():
    barRepo = BarRepo.BarRepo()
    results = barRepo.getAllBars()
    return  jsonify([e.toJson() for e in results])

def getbarTopBeerBrand(bar, dayOfWeek):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getbarTopBeerBrand(bar,dayOfWeek)
    return  jsonify([e.toJson() for e in results])


def getTopLargestSpenders(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getTopLargestSpenders(bar)
    return  jsonify([e.toJson() for e in results])

def getSaleDistributionDays(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getSaleDistributionDays(bar)
    return  jsonify([e.toJson() for e in results])

def getTimeDistrubition(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getTimeDistrubition(bar)
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
No bar can have the same name
check is implemented in table
'''
def insertBar(bar):
	barRepo = BarRepo.BarRepo()
	return barRepo.insertBar(bar)

'''
checks to make:
No bar can have the same name
check is implemented in table
'''
def updateBar(bar,oldName):
	barRepo = BarRepo.BarRepo()
	return barRepo.updateBar(bar,oldName)

''' no check cascade should be handled by table '''
def deleteBar(bar):
	barRepo = BarRepo.BarRepo()
	return barRepo.deleteBar(bar)
