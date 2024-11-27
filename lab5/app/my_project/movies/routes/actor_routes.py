from flask import Blueprint
from my_project.movies.controller.orders.actor_controller import ActorController


actor_bp = Blueprint("actors", __name__)
actor_controller = ActorController()

@actor_bp.route("/actors", methods=['GET'])
def get_actors():
    return actor_controller.get_all()

@actor_bp.route("/actors/<int:actor_id>", methods=['GET'])
def get_actor_by_id(actor_id):
    return actor_controller.get_by_id(actor_id)

@actor_bp.route("/actors", methods=['POST'])
def add_actor():
    return actor_controller.create()

@actor_bp.route("/actors/<int:actor_id>", methods=['PATCH'])
def update_actor(actor_id):
    return actor_controller.update(actor_id)

@actor_bp.route("/actors/<int:actor_id>", methods=['DELETE'])
def delete_actor(actor_id):
    return actor_controller.delete(actor_id)
