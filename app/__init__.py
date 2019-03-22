from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_basicauth import BasicAuth
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jwt import JWT
from flask_login import LoginManager
from paynow import Paynow

app = Flask(__name__)

login_manager = LoginManager()
db = SQLAlchemy(app)
app.config.from_object('config')
ma = Marshmallow(app)
login_manager.init_app(app)
api = Api(app)
CORS(app)
paynow = Paynow(
    '7121', 
    '0fbc8fd5-2624-474f-8752-10ff4ee2d463',
    'https://www.google.com', 
    'httpw://www.google.com'
)


app.config['BASIC_AUTH_USERNAME'] = 'purple'
app.config['BASIC_AUTH_PASSWORD'] = 'purple'



basic_auth = BasicAuth(app)

from . import views

from .auth import auth
from .api import api
from .admin import admin
from .web import web


app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(api)
app.register_blueprint(web)