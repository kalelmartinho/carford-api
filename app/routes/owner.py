from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models.owner import Owner
from app.models.car import Car



owner_bp = Blueprint("owner", __name__, url_prefix="/owners")


@owner_bp.before_request
@jwt_required()
def verify_token():
    pass

@owner_bp.route("/", methods=["POST"])
def create_owner():
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Missing name parameter"}), 400

    owner = Owner(name=name)
    db.session.add(owner)
    db.session.commit()

    return jsonify({"owner_id": owner.id, "name": owner.name}), 201

@owner_bp.route("/<int:owner_id>", methods=["PUT"])
def update_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    data = request.json
    new_name = data.get("name")

    if not new_name:
        return jsonify({"error": "Missing name parameter"}), 400

    owner.name = new_name
    db.session.commit()

    return jsonify({"owner_id": owner.id, "name": owner.name}), 200

@owner_bp.route("/", methods=["GET"])
def get_all_owners():
    owners = Owner.query.all()
    response = []

    for owner in owners:
        response.append({"owner_id": owner.id, "name": owner.name, "has_car": owner.has_car})

    return jsonify(response), 200


@owner_bp.route("/<int:owner_id>", methods=["GET"])
def get_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    return jsonify({"owner_id": owner.id, "name": owner.name, "has_car": owner.has_car}), 200




@owner_bp.route("/<int:owner_id>", methods=["DELETE"])
def delete_owner(owner_id):
    """Delete owner and all his cars from db"""
    owner = Owner.query.get_or_404(owner_id)
    cars = Car.query.filter_by(owner_id=owner.id).all()
    for car in cars:
        db.session.delete(car)
    db.session.delete(owner)
    db.session.commit()
    return jsonify({'message': f'Owner with id {owner_id} has been deleted'}), 204

