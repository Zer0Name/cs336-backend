from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable

dailyController = Blueprint('dailyController', __name__)

import v1.Services.InventoryService as inventoryService
import v1.Services.ShiftsService as shiftsService
import v1.Services.OperatesService as operatesService


@dailyController.route('/update/inventory', methods=['POST'])
def updateInventoryForToday():
    return inventoryService.insertInventoryForToday()


@dailyController.route('/update/shifts', methods=['POST'])
def updateShiftsForToday():
    return shiftsService.insertShiftsForToday()


@dailyController.route('/update/operates', methods=['POST'])
def updateOperatesForToday():
    return operatesService.insertOperatesForToday()

