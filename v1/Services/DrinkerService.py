from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.DrinkersRepo as DrinkerRepo

def getAllDrinkers():
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getAllDrinkers()
    return  jsonify([e.toJson() for e in results])

def getDrinkerTransactions(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerTransactions(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerTopBeer(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerTopBeer(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerBarSpending(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerBarSpending(drinker)
    return  jsonify([e.toJson() for e in results])  


def getDrinkerSpendingByDay(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerSpendingByDay(drinker)
    return  jsonify([e.toJson() for e in results])  


def getDrinkerSpendingByWeek(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerSpendingByWeek(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerSpendingByMonth(drinker):
    drinkerRepo = DrinkerRepo.DrinkerRepo()
    results = drinkerRepo.getDrinkerSpendingByMonth(drinker)
    return  jsonify([e.toJson() for e in results])  

'''
checks to make:
No drinker can have the same name
check is implemented in table
'''
def insertDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.insertDrinker(drinker)

'''
checks to make:
No drinker can have the same name
check is implemented in table
'''
def updateDrinker(drinker,oldName):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.updateDrinker(drinker,oldName)

''' no check cascade should be handled by table '''
def deleteDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.deleteDrinker(drinker)
