from flask import Blueprint
from ..controller.orders.nomination_controllers import NominationController

nomination_bp = Blueprint("nominations", __name__)
nomination_controller = NominationController()


@nomination_bp.route("/nominations", methods=['GET'])
def get_nominations():
    return nomination_controller.get_all()

@nomination_bp.route("/nominations/<int:nomination_id>", methods=['GET'])
def get_nomination_by_id(nomination_id):
    return nomination_controller.get_by_id(nomination_id)

@nomination_bp.route("/nominations", methods=['POST'])
def add_nomination():
    return nomination_controller.create()

@nomination_bp.route("/nominations/<int:nomination_id>", methods=['PATCH'])
def update_nomination(nomination_id):
    return nomination_controller.update(nomination_id)

@nomination_bp.route("/nominations/<int:nomination_id>", methods=['DELETE'])
def delete_nomination(nomination_id):
    return nomination_controller.delete(nomination_id)

