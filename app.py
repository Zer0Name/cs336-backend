from flask import Flask
from flask import jsonify

from v1.Controllers.VersionController import versionController
from v1.Controllers.DrinkerController import drinkerController
from v1.Controllers.BarController import barController
from v1.Controllers.BeerController import beerController
from v1.Controllers.ModificationController import modificationController
from v1.Controllers.BartenderController import bartenderController
from v1.Controllers.ManufacturerController import manufacturerController
from v1.Controllers.DailyController import dailyController

from v1.Exceptions.DrinkerNotFound import DrinkerNotFound
from v1.Exceptions.InvalidInfo import InvalidInfo
from v1.Exceptions.BarNotFound import BarNotFound
from v1.Exceptions.Error import Error
from v1.Exceptions.MissingParamaters import MissingParamaters

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.register_blueprint(dailyController,url_prefix='/v1/daily')
app.register_blueprint(versionController,url_prefix='/v1/version')
app.register_blueprint(drinkerController,url_prefix='/v1/drinker')
app.register_blueprint(barController,url_prefix='/v1/bar')
app.register_blueprint(beerController,url_prefix='/v1/beer')
app.register_blueprint(modificationController,url_prefix='/v1/modification')
app.register_blueprint(bartenderController,url_prefix='/v1/bartender')
app.register_blueprint(manufacturerController,url_prefix='/v1/manufacturer')

@app.errorhandler(MissingParamaters)
@app.errorhandler(Error)
@app.errorhandler(InvalidInfo)
@app.errorhandler(DrinkerNotFound)
@app.errorhandler(BarNotFound)
def CreateUserException(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


import v1.Repos.OperatesRepo as OperatesRepo

@app.route('/')
def hello_world():
	# operatesRepo = OperatesRepo.OperatesRepo()
	# results = operatesRepo.updateIncorrectOperates()
	return "hello chris I am your master"



#app.run(debug = True, port=8000)
