from flask import Blueprint, jsonify
from ..controller.orders.studio_controller import StudioController


studio_bp = Blueprint("studios", __name__)
studio_controller = StudioController()

@studio_bp.route("/studios", methods=['GET'])
def get_studios():
    return studio_controller.get_all()

@studio_bp.route("/studios/<int:studio_id>", methods=['GET'])
def get_studio_by_id(studio_id):
    return studio_controller.get_by_id(studio_id)

@studio_bp.route("/studios/<int:studio_id>/movies", methods=['GET'])
def get_movies_by_studio(studio_id):
    return jsonify(studio_controller.service.get_movies_by_studio_id(studio_id))

@studio_bp.route("/studios", methods=['POST'])
def add_studio():
    return studio_controller.create()

@studio_bp.route("/studios/<int:studio_id>", methods=['PATCH'])
def update_studio(studio_id):
    return studio_controller.update(studio_id)

@studio_bp.route("/studios/<int:studio_id>", methods=['DELETE'])
def delete_studio(studio_id):
    return studio_controller.delete(studio_id)
