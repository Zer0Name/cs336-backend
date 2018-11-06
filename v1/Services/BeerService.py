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
