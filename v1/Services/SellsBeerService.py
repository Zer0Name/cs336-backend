from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsBeerRepo as SellsBeerRepo
import v1.DTO.TrueFalseDTO as TrueFalseDTO
from v1.Exceptions.Error import Error

def getAllSellsBeer():
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.getAllSellsBeer()
	return  jsonify([e.toJson() for e in results])

def getAllBeersAndPrices(bar):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.getAllBeersAndPrices(bar)
	return  jsonify([e.toJson() for e in results])

def get_price_for_quantity(bar, beer, quantity):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.get_price_for_quantity(bar, beer, quantity)
	return  jsonify(str(results))

def get_price(bar,beer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.get_price(bar, beer)
	return  jsonify(str(results))

def get_beers_for_bar(bar):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.get_beers_for_bar(bar)
	return  jsonify([e.toJson() for e in results])

def get_bar_for_beers(beer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
	results = sellsBeerRepo.get_bar_for_beers(beer)
	return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
beer exists
bar exists
pattern #3
'''
def insertSellsBeer(sellsBeer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	if sellsBeerRepo.duplicate_entry(sellsBeer.getBeername(), sellsBeer.getBarname()):
		raise Error("Duplicate Entry")
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	return sellsBeerRepo.insertSellsBeer(sellsBeer)
	

'''
checks to make:
no duplicate entries
beer exists
bar exists
pattern #3
'''
def updateSellsBeer(sellsBeer,oldBeer, oldBar):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	if sellsBeerRepo.duplicate_entry(sellsBeer.getBeername(), sellsBeer.getBarname()) and (not oldBeer == sellsBeer.getBeername() or not oldBar == sellsBeer.getBarname()):
		raise Error("Duplicate Entry")
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	return sellsBeerRepo.updateSellsBeer(sellsBeer, oldBeer, oldBar)

''' no check cascade should be handled by table '''
def deleteSellsBeer(sellsBeer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	return sellsBeerRepo.deleteSellsBeer(sellsBeer)

