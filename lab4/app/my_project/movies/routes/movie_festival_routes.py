from flask import Blueprint
from my_project.movies.controller.orders.movie_festival_controller import MovieFestivalController

movie_festival_bp = Blueprint("movie_festival", __name__)
movie_festival_controller = MovieFestivalController()


@movie_festival_bp.route("/movie_festival", methods=['GET'])
def get_movie_festival():
    return movie_festival_controller.get_all()

@movie_festival_bp.route("/movie_festival/<int:festival_id>/<int:movie_id>", methods=['GET'])
def get_movie_festival_by_id(festival_id, movie_id):
    return movie_festival_controller.get_by_id((festival_id, movie_id))

@movie_festival_bp.route("/movie_festival/all", methods=["GET"])
def get_movies_for_each_festival():
    return movie_festival_controller.get_movies_for_each_festival()


@movie_festival_bp.route("/movie_festival", methods=['POST'])
def add_movie_festival():
    return movie_festival_controller.create()

@movie_festival_bp.route("/movie_festival/<int:festival_id>/<int:movie_id>", methods=['PATCH'])
def update_movie_festival(festival_id, movie_id):
    return movie_festival_controller.update((festival_id, movie_id))

@movie_festival_bp.route("/movie_festival/<int:festival_id>/<int:movie_id>", methods=['DELETE'])
def delete_movie_festival(festival_id, movie_id):
    return movie_festival_controller.delete((festival_id, movie_id))
