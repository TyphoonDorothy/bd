from flask import Blueprint
from my_project.movies.controller.orders.movie_genre_controller import MovieAwardController


movie_genre_bp = Blueprint("movie_genre", __name__)
movie_genre_controller = MovieAwardController()


@movie_genre_bp.route("/movie_genre", methods=['GET'])
def get_movie_genre():
    return movie_genre_controller.get_all()

@movie_genre_bp.route("/movie_genre/<int:genre_id>/<int:movie_id>", methods=['GET'])
def get_movie_genre_by_id(genre_id, movie_id):
    return movie_genre_controller.get_by_id((genre_id, movie_id))

@movie_genre_bp.route("/movie_genre/all", methods=['GET'])
def get_movies_for_each_genre():
    return movie_genre_controller.get_movies_for_each_genre()

@movie_genre_bp.route("/movie_genre", methods=['POST'])
def add_movie_genre():
    return movie_genre_controller.create()

@movie_genre_bp.route("/movie_genre/<int:genre_id>/<int:movie_id>", methods=['PATCH'])
def update_movie_genre(genre_id, movie_id):
    return movie_genre_controller.update((genre_id, movie_id))

@movie_genre_bp.route("/movie_genre/<int:genre_id>/<int:movie_id>", methods=['DELETE'])
def delete_movie_genre(genre_id, movie_id):
    return movie_genre_controller.delete((genre_id, movie_id))
