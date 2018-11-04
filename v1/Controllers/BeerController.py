from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Services.BeerService as beerService

beerController = Blueprint('beerController', __name__)

@beerController.route('', methods=['GET'])
def getAllBeers():
    return beerService.getAllBeers()