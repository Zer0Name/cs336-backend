from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.DrinkersRepo as DrinkersRepo

def getAllDrinkers():
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getAllDrinkers()
    return  jsonify([e.toJson() for e in results])

def getDrinkerTransactions(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerTransactions(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerTopBeer(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerTopBeer(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerBarSpending(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerBarSpending(drinker)
    return  jsonify([e.toJson() for e in results])  


def getDrinkerSpendingByDay(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerSpendingByDay(drinker)
    return  jsonify([e.toJson() for e in results])  


def getDrinkerSpendingByWeek(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerSpendingByWeek(drinker)
    return  jsonify([e.toJson() for e in results])  

def getDrinkerSpendingByMonth(drinker):
    drinkerRepo = DrinkersRepo.DrinkersRepo()
    results = drinkerRepo.getDrinkerSpendingByMonth(drinker)
    return  jsonify([e.toJson() for e in results])  

'''
checks to make:
No drinker can have the same name
check is implemented in table

Check that no bartender has the same name (and phone number?)
'''
def insertDrinker(drinker):
	drinkerRepo = DrinkersRepo.DrinkersRepo()
	return drinkerRepo.insertDrinker(drinker)

'''
checks to make:
No drinker can have the same name
check is implemented in table

Check that no bartender has the same name (and phone number?)
'''
def updateDrinker(drinker,oldName):
	drinkerRepo = DrinkersRepo.DrinkersRepo()
	return drinkerRepo.updateDrinker(drinker,oldName)

''' no check cascade should be handled by table '''
def deleteDrinker(drinker):
	drinkerRepo = DrinkersRepo.DrinkersRepo()
	return drinkerRepo.deleteDrinker(drinker)
