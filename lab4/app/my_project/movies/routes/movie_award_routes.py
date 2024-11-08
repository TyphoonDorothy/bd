from flask import Blueprint
from my_project.movies.controller.orders.movie_award_controller import MovieAwardController


movie_award_bp = Blueprint("movie_award", __name__)
movie_award_controller = MovieAwardController()


@movie_award_bp.route("/movie_award", methods=['GET'])
def get_movie_award():
    return movie_award_controller.get_all()

@movie_award_bp.route("/movie_award/<int:award_id>/<int:movie_id>", methods=['GET'])
def get_movie_award_by_id(award_id, movie_id):
    return movie_award_controller.get_by_id((award_id, movie_id))

@movie_award_bp.route("/movie_award/all", methods=['GET'])
def get_movies_for_each_award():
    return movie_award_controller.get_movies_for_each_award()

@movie_award_bp.route("/movie_award", methods=['POST'])
def add_movie_award():
    return movie_award_controller.create()

@movie_award_bp.route("/movie_award/<int:award_id>/<int:movie_id>", methods=['PATCH'])
def update_movie_award(award_id, movie_id):
    return movie_award_controller.update((award_id, movie_id))

@movie_award_bp.route("/movie_award/<int:award_id>/<int:movie_id>", methods=['DELETE'])
def delete_movie_award(award_id, movie_id):
    return movie_award_controller.delete((award_id, movie_id))
