from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity



app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)
