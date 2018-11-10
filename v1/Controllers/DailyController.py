from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable

dailyController = Blueprint('dailyController', __name__)

import v1.Services.InventoryService as inventoryService


@dailyController.route('/update/inventory', methods=['POST'])
def updateInventoryForToday():
    return inventoryService.insertInventoryForToday()