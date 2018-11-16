from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsFoodRepo as SellsFoodRepo
from v1.Exceptions.Error import Error

def getAllSellsFood():
    sellsFoodRepo = SellsFoodRepo.SellsFoodRepo() 
    results = sellsFoodRepo.getAllSellsFood()
    return  jsonify([e.toJson() for e in results])

def get_price_for_quantity(bar, food, quantity):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo() 
	results = sellsFoodRepo.get_price_for_quantity(bar, food, quantity)
	return  jsonify(str(results))

def get_price(bar,food):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo() 
	results = sellsFoodRepo.get_price(bar, food)
	return  jsonify(str(results))

def get_foods_for_bar(bar):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()  
	results = sellsFoodRepo.get_foods_for_bar(bar)
	return  jsonify([e.toJson() for e in results])

def get_bars_for_foods(food):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()  
	results = sellsFoodRepo.get_bars_for_foods(food)
	return  jsonify([e.toJson() for e in results])

def getAllFoodAndPrices(bar):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()  
	results = sellsFoodRepo.getAllFoodAndPrices(bar)
	return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
Food exists
bar exists
'''
def insertSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	if sellsFoodRepo.duplicate_entry(sellsFood.getFoodname(), sellsFood.getBarname()):
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
	if sellsFoodRepo.duplicate_entry(sellsFood.getFoodname(), sellsFood.getBarname()) and (not oldFood == sellsFood.getFoodname() or not oldBar == sellsFood.getBarname()):
		raise Error("Duplicate Entry")
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.updateSellsFood(sellsFood, oldFood, oldBar)

''' no check cascade should be handled by table '''
def deleteSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.deleteSellsFood(sellsFood)