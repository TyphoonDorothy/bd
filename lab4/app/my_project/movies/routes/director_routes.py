from flask import Blueprint, jsonify
from my_project.movies.controller.orders.director_controller import DirectorController


director_bp = Blueprint("director", __name__)
director_controller = DirectorController()

@director_bp.route("/directors", methods=["GET"])
def get_directors():
    return director_controller.get_all()

@director_bp.route("/directors/<int:director_id>", methods=["GET"])
def get_director_by_id(director_id):
    return director_controller.get_by_id(director_id)

@director_bp.route("/directors/<int:director_id>/movies", methods=['GET'])
def get_movies_by_director(director_id):
    return jsonify(director_controller.service.get_movies_by_director_id(director_id))

@director_bp.route("/directors", methods=["POST"])
def add_director():
    return director_controller.create()

@director_bp.route("/directors/<int:director_id>", methods=["PATCH"])
def update_director(director_id):
    return director_controller.update(director_id)

@director_bp.route("/directors/<int:director_id>", methods=["DELETE"])
def delete_director(director_id):
    return director_controller.delete(director_id)
