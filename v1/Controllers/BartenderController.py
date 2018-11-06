from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
import v1.Services.BartenderService as bartenderService
from v1.Exceptions.InvalidInfo import InvalidInfo

bartenderController = Blueprint('bartenderController', __name__)

@bartenderController.route('', methods=['GET'])
def getAllBartenders():
    return bartenderService.getAllBartenders()

@bartenderController.route('/shifts/past', methods=['GET'])
def getAllPastShifts():
    bartender = str(request.args.get('bartender'))
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bartender) or variable.isEmpty(bar):
        raise InvalidInfo("bartender or bar not provided") 
    return bartenderService.getAllPastShifts(bartender, bar)

@bartenderController.route('/sold/beer/brands', methods=['GET'])
def getNumberOfEachBeerBrandSold():
    bartender = str(request.args.get('bartender'))
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bartender) or variable.isEmpty(bar):
        raise InvalidInfo("bartender or bar not provided") 
    return bartenderService.getNumberOfEachBeerBrandSold(bartender, bar)

@bartenderController.route('/rank/sold/beers', methods=['GET'])
def rankByNumberOfBeersSold():
    startTime = str(request.args.get('startTime'))
    endTime = str(request.args.get('endTime'))
    day = str(request.args.get('day'))
    bar = str(request.args.get('bar'))
    if variable.isEmpty(startTime) or variable.isEmpty(endTime) or variable.isEmpty(day) or variable.isEmpty(bar):
        raise InvalidInfo("startTime, endTime, day, or bar not provided") 
    return bartenderService.rankByNumberOfBeersSold(startTime, endTime, day, bar)