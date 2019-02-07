from flask import Blueprint

web = Blueprint('web', __name__, url_prefix='/web')

from . import views
