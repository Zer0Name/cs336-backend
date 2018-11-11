from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsBeerRepo as SellsBeerRepo

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
	return sellsBeerRepo.updateSellsBeer(sellsBeer, oldBeer, oldBar)

''' no check cascade should be handled by table '''
def deleteSellsBeer(sellsBeer):
	sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
	return sellsBeerRepo.deleteSellsBeer(sellsBeer)