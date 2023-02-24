from flask import Blueprint, jsonify, request
from app import db
from app.models.owner import Owner

owner_bp = Blueprint('owner', __name__, url_prefix='/owner')

@owner_bp.route('/', methods=['GET'])
def get_all_owners():
    owners = Owner.query.all()
    return jsonify([owner.to_dict() for owner in owners]), 200

@owner_bp.route('/', methods=['POST'])
def create_owner():
    data = request.get_json()
    owner = Owner(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(owner)
    db.session.commit()
    return jsonify(owner.to_dict()), 201

@owner_bp.route('/<int:owner_id>', methods=['GET'])
def get_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner is None:
        return jsonify({'error': 'Owner not found'}), 404
    return jsonify(owner.to_dict()), 200

@owner_bp.route('/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner is None:
        return jsonify({'error': 'Owner not found'}), 404
    data = request.get_json()
    owner.name = data['name']
    owner.email = data['email']
    owner.phone = data['phone']
    db.session.commit()
    return jsonify(owner.to_dict()), 200

@owner_bp.route('/<int:owner_id>', methods=['DELETE'])
def delete_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner is None:
        return jsonify({'error': 'Owner not found'}), 404
    db.session.delete(owner)
    db.session.commit()
    return '', 204
