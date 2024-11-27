from flask import Blueprint
from ..controller.orders.festival_controller import FestivalController


festival_bp = Blueprint("festivals", __name__)
festival_controller = FestivalController()

@festival_bp.route("/festivals", methods=["GET"])
def get_festivals():
    return festival_controller.get_all()

@festival_bp.route("/festivals/<int:festival_id>", methods=["GET"])
def get_festival_by_id(festival_id):
    return festival_controller.get_by_id(festival_id)

@festival_bp.route("/festivals", methods=["POST"])
def add_festival():
    return festival_controller.create()

@festival_bp.route("/festivals/<int:festival_id>", methods=["PATCH"])
def update_festival(festival_id):
    return festival_controller.update(festival_id)

@festival_bp.route("/festivals/<int:festival_id>", methods=["DELETE"])
def delete_festival(festival_id):
    return festival_controller.delete(festival_id)
