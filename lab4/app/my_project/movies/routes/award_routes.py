from flask import Blueprint
from ..controller.orders.award_controller import AwardController


award_bp = Blueprint("awards", __name__)
award_controller = AwardController()

@award_bp.route("awards", methods=["GET"])
def get_awards():
    return award_controller.get_all()

@award_bp.route("/awards/<int:award_id>", methods=["GET"])
def get_award_by_id(award_id):
    return award_controller.get_by_id(award_id)

@award_bp.route("/awards", methods=["POST"])
def add_award():
    return award_controller.create()

@award_bp.route("/awards/<int:award_id>", methods=["PATCH"])
def update_award(award_id):
    return award_controller.update(award_id)

@award_bp.route("/awards/<int:award_id>", methods=["DELETE"])
def delete_award(award_id):
    return award_controller.delete(award_id)
