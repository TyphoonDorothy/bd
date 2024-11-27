from flask import Blueprint
from ..controller.orders.fact_controller import FactController


fact_bp = Blueprint("facts", __name__)
fact_controller = FactController()

@fact_bp.route("/facts", methods=["GET"])
def get_facts():
    return fact_controller.get_all()

@fact_bp.route("/facts/<int:fact_id>", methods=["GET"])
def get_fact_by_id(fact_id):
    return fact_controller.get_by_id(fact_id)

@fact_bp.route("/facts", methods=["POST"])
def add_fact():
    return fact_controller.create()

@fact_bp.route("/facts/<int:fact_id>", methods=["PATCH"])
def update_fact(fact_id):
    return fact_controller.update(fact_id)

@fact_bp.route("/facts/<int:fact_id>", methods=["DELETE"])
def delete_fact(fact_id):
    return fact_controller.delete(fact_id)
