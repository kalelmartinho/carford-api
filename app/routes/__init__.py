from flask import Blueprint

from .car import car_bp
from .owner import owner_bp
from .auth import auth_bp


api_bp = Blueprint('api', __name__)
api_bp.register_blueprint(car_bp)
api_bp.register_blueprint(owner_bp)
