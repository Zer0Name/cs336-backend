from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime

versionController = Blueprint('versionController', __name__)

@versionController.route('', methods=['GET'])
def version():
    return jsonify({"version": "0.1.2","date_time" : str((datetime.datetime.utcnow() - datetime.timedelta(hours=4))) })