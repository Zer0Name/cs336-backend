from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
import v1.Services.ManufacturerService as manufacturerService
from v1.Exceptions.InvalidInfo import InvalidInfo

manufacturerController = Blueprint('manufacturerController', __name__)

@manufacturerController.route('', methods=['GET'])
def getAllManufacturers():
	return manufacturerService.getAllManufacturers()

@manufacturerController.route('/beers', methods=['GET'])
def getAllBeersByManufacturer():
	manf = str(request.args.get('manf'))
	if variable.isEmpty(manf):
		raise InvalidInfo("manufacturer not provided") 
	return manufacturerService.getAllBeersByManufacturer(manf)

@manufacturerController.route('/sales/lastweek/top/states', methods=['GET'])
def getTop10StatesWithHighestSalesInTheLastWeek():
	manf = str(request.args.get('manf'))
	if variable.isEmpty(manf):
		raise InvalidInfo("manufacturer not provided") 
	return manufacturerService.getTop10StatesWithHighestSalesInTheLastWeek(manf)

@manufacturerController.route('liked/top/states', methods=['GET'])
def getTop10StatesWhereTheirBeerIsLikedTheMost():
	manf = str(request.args.get('manf'))
	if variable.isEmpty(manf):
		raise InvalidInfo("manufacturer not provided") 
	return manufacturerService.getTop10StatesWhereTheirBeerIsLikedTheMost(manf)