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
    '6389', 
    '8db834f2-8a94-40a5-a716-e3f5bbfe4a37',
    'http://google.com', 
    'http://google.com'
    )


app.config['BASIC_AUTH_USERNAME'] = 'purple'
app.config['BASIC_AUTH_PASSWORD'] = 'purple'



basic_auth = BasicAuth(app)
from . import views, models, app, db