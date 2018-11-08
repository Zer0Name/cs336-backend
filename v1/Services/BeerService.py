from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BeerRepo as BeerRepo

def getAllBeers():
    beerRepo = BeerRepo.BeerRepo()
    results = beerRepo.getAllBeers()
    return  jsonify([e.toJson() for e in results])


def getBarsWhichSoldTheMost(beer):
    beerRepo = BeerRepo.BeerRepo()
    results = beerRepo.getBarsWhichSoldTheMost(beer)
    return  jsonify([e.toJson() for e in results])


def getBiggestConsumers(beer):
    beerRepo = BeerRepo.BeerRepo()
    results = beerRepo.getBiggestConsumers(beer)
    return  jsonify([e.toJson() for e in results])

def getTimeDistrubition(beer):
    beerRepo = BeerRepo.BeerRepo()
    results = beerRepo.getTimeDistrubition(beer)
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
No beer can have the same name
check is implemented in table
'''
def insertBeer(beer):
	beerRepo = BeerRepo.BeerRepo()
	return beerRepo.insertBeer(beer)

'''
checks to make:
No beer can have the same name
check is implemented in table
'''
def updateBeer(beer,oldName):
	beerRepo = BeerRepo.BeerRepo()
	return beerRepo.updateBeer(beer,oldName)

''' no check cascade should be handled by table '''
def deleteBeer(beer):
	beerRepo = BeerRepo.BeerRepo()
	return beerRepo.deleteBeer(beer)
