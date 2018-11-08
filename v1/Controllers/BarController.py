from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
import v1.Services.BarService as barService
from v1.Exceptions.InvalidInfo import InvalidInfo

barController = Blueprint('barController', __name__)


@barController.route('', methods=['GET'])
def getAllBars():
    return barService.getAllBars()

@barController.route('/inventory/fraction', methods=['GET'])
def getAllFractionsOfInventory():
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bar):
        raise InvalidInfo("bar was not provided")
    return barService.getAllFractionsOfInventory(bar)

@barController.route('/beer/top', methods=['GET'])
def topBeer():
    bar = str(request.args.get('bar'))
    dayOfWeek = str(request.args.get('day_of_week'))
    if variable.isEmpty(bar) or variable.isEmpty(dayOfWeek):
        raise InvalidInfo("bar or day of the week was not provided")
    return barService.getbarTopBeerBrand(bar,dayOfWeek)

@barController.route('/top/spenders', methods=['GET'])
def topLargestSpenders():
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bar):
        raise InvalidInfo("bar not provided") 
    return barService.getTopLargestSpenders(bar)

@barController.route('/sale/distribution/days', methods=['GET'])
def saleDistributioDays():
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bar):
        raise InvalidInfo("bar not provided") 
    return barService.getSaleDistributionDays(bar)


@barController.route('/sale/time/distribution', methods=['GET'])
def getTimedistribution():
    bar = str(request.args.get('bar'))
    if variable.isEmpty(bar):
        raise InvalidInfo("bar not provided")
    return barService.getTimeDistrubition(bar)