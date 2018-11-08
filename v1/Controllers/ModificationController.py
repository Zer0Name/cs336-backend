from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

import v1.Services.ModificationService as modificationService
import v1.Services.BeerService as beerService

from v1.Entity.Drinker import Drinker
from v1.Entity.Beer import Beer

import v1.Services.DrinkerService as drinkerService

modificationController = Blueprint('modificationController', __name__)



# --------------------- DRINKER ------------------------------
@modificationController.route('/drinker/insert', methods=['POST'])
def insertDrinker():
	drinker = Drinker()
	drinker.requestMap(request.get_json())
	return drinkerService.insertDrinker(drinker)

@modificationController.route('/drinker/update', methods=['POST'])
def updateDrinker():
	drinker = Drinker()
	req = request.get_json()
	drinker.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return drinkerService.updateDrinker(drinker,oldName)

@modificationController.route('/drinker/delete', methods=['POST'])
def deleteDrinker():
	drinker = Drinker()
	drinker.requestMap(request.get_json())
	return drinkerService.deleteDrinker(drinker)

# --------------------- BEER ------------------------------
@modificationController.route('/beer/insert', methods=['POST'])
def insertBeer():
	beer = Beer()
	beer.requestMap(request.get_json())
	return beerService.insertBeer(beer)

@modificationController.route('/beer/update', methods=['POST'])
def updateBeer():
	beer = Beer()
	req = request.get_json()
	beer.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return beerService.updateBeer(beer,oldName)

@modificationController.route('/beer/delete', methods=['POST'])
def deleteBeer():
	beer = Beer()
	beer.requestMap(request.get_json())
	return beerService.deleteBeer(beer)