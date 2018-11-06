from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BarRepo as BarRepo


def getAllBars():
    barRepo = BarRepo.BarRepo()
    results = barRepo.getAllBars()
    return  jsonify([e.toJson() for e in results])

def getbarTopBeerBrand(bar, dayOfWeek):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getbarTopBeerBrand(bar,dayOfWeek)
    return  jsonify([e.toJson() for e in results])


def getTopLargestSpenders(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getTopLargestSpenders(bar)
    return  jsonify([e.toJson() for e in results])



def getSaleDistributionDays(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getSaleDistributionDays(bar)
    return  jsonify([e.toJson() for e in results])

def getTimeDistrubition(bar):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getTimeDistrubition(bar)
    return  jsonify([e.toJson() for e in results])
