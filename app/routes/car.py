from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy import exc

from app.models.car import Car
from app.models.owner import Owner
from app import db

car_bp = Blueprint('car', __name__, url_prefix='/cars')


@car_bp.before_request
@jwt_required()
def verify_token():
    pass

@car_bp.route('/', methods=['GET'])
def get_all_cars():
    cars = Car.query.all()
    return jsonify({'cars': [car.to_dict() for car in cars]})

@car_bp.route('/', methods=['POST'])
def add_car():
    data = request.get_json()
    owner_id = data.get('owner_id')
    if not owner_id:
        return jsonify({'error': 'owner_id is required'}), 400
    owner = Owner.query.get(owner_id)
    if not owner:
        return jsonify({'error': f'Owner with id {owner_id} not found'}), 404
    if len(owner.cars) >= 3:
        return jsonify({'error': f'Owner {owner.name} already has the maximum number of cars (3)'}), 400
    car = Car(color=data.get('color'), model=data.get('model'))
    owner.cars.append(car)
    db.session.add(car)
    db.session.commit()
    return jsonify({'car': car.to_dict()}), 201

@car_bp.route('/<int:id>', methods=['GET'])
def get_car(id):
    car = Car.query.get(id)
    if not car:
        return jsonify({'error': f'Car with id {id} not found'}), 404
    return jsonify({'car': car.to_dict()})

@car_bp.route('/<int:id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get(id)
    if not car:
        return jsonify({'error': f'Car with id {id} not found'}), 404
    data = request.get_json()
    color = data.get('color')
    model = data.get('model')
    if color:
        car.color = color
    if model:
        car.model = model
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Could not update car'}), 500
    return jsonify({'car': car.to_dict()})

@car_bp.route('/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    if not car:
        return jsonify({'error': f'Car with id {id} not found'}), 404
    db.session.delete(car)
    db.session.commit()
    return '', 204