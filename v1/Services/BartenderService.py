from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BartenderRepo as BartenderRepo

def getAllBartenders():
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getAllBartenders()
    return  jsonify([e.toJson() for e in results])

def getAllPastShifts(bartender,bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getAllPastShifts(bartender,bar)
    return  jsonify([e.toJson() for e in results])

def getNumberOfEachBeerBrandSold(bartender,bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.getNumberOfEachBeerBrandSold(bartender,bar)
    return  jsonify([e.toJson() for e in results])

def rankByNumberOfBeersSold(startTime, endTime, day, bar):
    bartenderRepo = BartenderRepo.BartenderRepo()
    results = bartenderRepo.rankByNumberOfBeersSold(startTime, endTime, day, bar)
    return  jsonify([e.toJson() for e in results])
