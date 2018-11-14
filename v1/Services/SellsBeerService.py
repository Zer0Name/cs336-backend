from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsBeerRepo as SellsBeerRepo
import v1.DTO.TrueFalseDTO as TrueFalseDTO
from v1.Exceptions.Error import Error

def getAllSellsBeer():
    sellsBeerRepo = SellsBeerRepo.SellsBeerRepo() 
    results = sellsBeerRepo.getAllSellsBeer()
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
	#return sellsBeerRepo.insertSellsBeer(sellsBeer)
	return "hello"

'''
checks to make:
no duplicate entries
beer exists
bar exists
pattern #3
'''
def updateSellsBeer(sellsBeer,oldBeer, oldBar):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	if sellsBeerRepo.duplicate_entry(sellsBeer.getBeer(), sellsBeer.getBar()) and (not oldBeer == sellsBeer.getBeer() or not oldBar == sellsBeer.getBar()):
		raise Error("Duplicate Entry")
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	#return sellsBeerRepo.updateSellsBeer(sellsBeer, oldBeer, oldBar)
	return "hello"

''' no check cascade should be handled by table '''
def deleteSellsBeer(sellsBeer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	return sellsBeerRepo.deleteSellsBeer(sellsBeer)

