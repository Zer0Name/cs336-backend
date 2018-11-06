from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
import v1.Services.BeerService as beerService
from v1.Exceptions.InvalidInfo import InvalidInfo

beerController = Blueprint('beerController', __name__)

@beerController.route('', methods=['GET'])
def getAllBeers():
    return beerService.getAllBeers()


@beerController.route('/biggest/consumers', methods=['GET'])
def getBiggestConsumers():
    beer = str(request.args.get('beer'))
    if variable.isEmpty(beer):
        raise InvalidInfo("beer not provided") 
    return beerService.getBiggestConsumers(beer)

@beerController.route('/sold/most', methods=['GET'])
def getBarsWhichSoldTheMost():
    beer = str(request.args.get('beer'))
    if variable.isEmpty(beer):
        raise InvalidInfo("beer not provided") 
    return beerService.getBarsWhichSoldTheMost(beer)