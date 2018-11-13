from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsFoodRepo as SellsFoodRepo
from v1.Exceptions.Error import Error

def getAllSellsFood():
    sellsFoodRepo = SellsFoodRepo.SellsFoodRepo() 
    results = sellsFoodRepo.getAllSellsFood()
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
Food exists
bar exists
'''
def insertSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	if sellsFoodRepo.duplicate_entry(sellsFood.getFood(), sellsFood.getBar()):
		raise Error("Duplicate Entry")
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.insertSellsFood(sellsFood)

'''
checks to make:
no duplicate entries
Food exists
bar exists
'''
def updateSellsFood(sellsFood,oldFood, oldBar):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	if sellsFoodRepo.duplicate_entry(sellsFood.getFood(), sellsFood.getBar()) and (not oldFood == sellsFood.getFood() or not oldBar == sellsFood.getBar()):
		raise Error("Duplicate Entry")
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.updateSellsFood(sellsFood, oldFood, oldBar)

''' no check cascade should be handled by table '''
def deleteSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.deleteSellsFood(sellsFood)