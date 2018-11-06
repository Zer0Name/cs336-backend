from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.InvalidInfo import InvalidInfo

import v1.Services.ModificationService as modificationService

from v1.Entity.Drinker import Drinker

modificationController = Blueprint('modificationController', __name__)


@modificationController.route('/drinker/insert', methods=['POST'])
def insertDrinker():
    drinker = Drinker()
    drinker.requestMap(request.get_json())
    return modificationService.insertDrinker(drinker)

@modificationController.route('/drinker/update', methods=['POST'])
def drinkerUpdate():
    drinker = Drinker()
    drinker.requestMap(request.get_json())
    return modificationService.updateDrinker(drinker)

@modificationController.route('/drinker/delete', methods=['POST'])
def drinkerDelete():
    drinker = Drinker()
    drinker.requestMap(request.get_json())
    return modificationService.deleteDrinker(drinker)