from flask import Flask
from flask import jsonify

from v1.Controllers.VersionController import versionController
from v1.Controllers.DrinkerController import drinkerController
from v1.Controllers.BarController import barController

from v1.Exceptions.DrinkerNotFound import DrinkerNotFound
from v1.Exceptions.InvalidInfo import InvalidInfo

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.register_blueprint(versionController,url_prefix='/v1/version')
app.register_blueprint(drinkerController,url_prefix='/v1/drinker')
app.register_blueprint(barController,url_prefix='/v1/bar')


@app.errorhandler(InvalidInfo)
@app.errorhandler(DrinkerNotFound)
def CreateUserException(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def hello_world():
    return "hello chris I am your master"



app.run(debug = True, port=8000)
