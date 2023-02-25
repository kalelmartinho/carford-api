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
    owner = Owner.query.get_or_404(owner_id)

    if owner.has_car:
        return jsonify({"error": "Cannot delete an owner with a car"}), 400

    db.session.delete(owner)
    db.session.commit()

    return "", 204


@owner_bp.route("/<int:owner_id>/add-car", methods=["POST"])
def add_car_to_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)

    if owner.has_car:
        return jsonify({"error": "Owner already has a car"}), 400

    data = request.json
    color = data.get("color")
    model = data.get("model")

    if not color or not model:
        return jsonify({"error": "Missing color or model parameter"}), 400

    if color not in ["yellow", "blue", "gray"]:
        return jsonify({"error": "Invalid color parameter"}), 400

    if model not in ["hatch", "sedan", "convertible"]:
        return jsonify({"error": "Invalid model parameter"}), 400

    car_count = Car.query.filter_by(owner_id=owner_id).count()

    if car_count >= 3:
        return jsonify({"error": "Owner already has 3 cars"}), 400

    car = Car(color=color, model=model, owner_id=owner_id)
    db.session.add(car)
    db.session.commit()

    owner.has_car = True
    db.session.commit()

    return jsonify({"car_id": car.id, "color": car.color, "model": car.model}), 201