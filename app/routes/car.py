from flask import Blueprint, jsonify, request
from app import db
from app.models.car import Car

car_bp = Blueprint('car', __name__, url_prefix='/car')

@car_bp.route('/', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars]), 200

@car_bp.route('/', methods=['POST'])
def create_car():
    data = request.json
    color = data.get('color')
    model = data.get('model')
    owner_id = data.get('owner_id')
    
    if not color or not model or not owner_id:
        return {'error': 'color, model, and owner_id are required fields'}, 400

    car = Car(color=color, model=model, owner_id=owner_id)
    db.session.add(car)
    db.session.commit()

    return jsonify(car.to_dict()), 201

@car_bp.route('/<int:id>', methods=['GET'])
def get_car(id):
    car = Car.query.get_or_404(id)
    return jsonify(car.to_dict()), 200

@car_bp.route('/<int:id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get_or_404(id)

    data = request.json
    color = data.get('color')
    model = data.get('model')
    owner_id = data.get('owner_id')

    if not color or not model or not owner_id:
        return {'error': 'color, model, and owner_id are required fields'}, 400

    car.color = color
    car.model = model
    car.owner_id = owner_id
    db.session.commit()

    return jsonify(car.to_dict()), 200

@car_bp.route('/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return '', 204
