from flask import Blueprint
from ..controller.orders.genre_controller import GenreController


genre_bp = Blueprint("genres", __name__)
genre_controller = GenreController()

@genre_bp.route("/genres", methods=["GET"])
def get_genres():
    return genre_controller.get_all()

@genre_bp.route("/genres/<int:genre_id>", methods=["GET"])
def get_genre_by_id(genre_id):
    return genre_controller.get_by_id(genre_id)

@genre_bp.route("/genres", methods=["POST"])
def add_genre():
    return genre_controller.create()

@genre_bp.route("/genres/<int:genre_id>", methods=["PATCH"])
def update_genre(genre_id):
    return genre_controller.update(genre_id)

@genre_bp.route("/genres/<int:genre_id>", methods=["DELETE"])
def delete_genre(genre_id):
    return genre_controller.delete(genre_id)
