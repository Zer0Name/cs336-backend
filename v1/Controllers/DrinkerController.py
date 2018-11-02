from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
from v1.Exceptions.DrinkerNotFound import DrinkerNotFound

import v1.Services.DrinkerService as drinkerService
import v1.Util.Variable as variable
import json

from v1.Exceptions.InvalidInfo import InvalidInfo

drinkerController = Blueprint('drinkerController', __name__)


@drinkerController.route('', methods=['GET'])
def getAllDrinkers():
    return drinkerService.getAllDrinkers()

@drinkerController.route('/transactions', methods=['GET'])
def getDrinkerTranscations():
    drinker = str(request.args.get('drinker'))
    if variable.isEmpty(drinker):
        raise InvalidInfo("Drinker not provided")
    return drinkerService.getDrinkerTransactions(drinker)

@drinkerController.route('/beer/top', methods=['GET'])
def getDrinkerTopBeer():
    drinker = str(request.args.get('drinker'))
    if variable.isEmpty(drinker):
        raise InvalidInfo("Drinker not provided")
    return drinkerService.getDrinkerTopBeer(drinker)

@drinkerController.route('/bar/spent/day', methods=['GET'])
def getDrinkerBarSpendingByDay():
    drinker = str(request.args.get('drinker'))
    if variable.isEmpty(drinker):
        raise InvalidInfo("Drinker not provided")
    return drinkerService.getDrinkerBarSpendingByDay(drinker)

@drinkerController.route('/bar/spent/week', methods=['GET'])
def getDrinkerBarSpendingByWeek():
    drinker = str(request.args.get('drinker'))
    if variable.isEmpty(drinker):
        raise InvalidInfo("Drinker not provided")
    return drinkerService.getDrinkerBarSpendingByWeek(drinker)

@drinkerController.route('/bar/spent/month', methods=['GET'])
def getDrinkerBarSpendingByMonth():
    drinker = str(request.args.get('drinker'))
    if variable.isEmpty(drinker):
        raise InvalidInfo("Drinker not provided")
    return drinkerService.getDrinkerBarSpendingByMonth(drinker)
    