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