from flask_restx  import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint, version="1.0", title="App Name")