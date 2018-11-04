from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Services.BarService as barService

barController = Blueprint('barController', __name__)

@barController.route('/top/beer', methods=['GET'])
def top():
    day = str(request.args.get('day'))
    dayOfWeek = str(request.args.get('day_of_week'))
    if variable.isEmpty(day) and variable.isEmpty(dayOfWeek):
        raise InvalidInfo("Drinker not provided")
    return barService.getbarTopBeerBrand(day,dayOfWeek)