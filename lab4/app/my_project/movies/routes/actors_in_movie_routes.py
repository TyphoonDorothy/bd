from flask import Blueprint
from my_project.movies.controller.orders.actors_in_movie_controller import ActorsInMovieController


actors_in_movie_bp = Blueprint("actors_in_movie", __name__)
actors_in_movie_controller = ActorsInMovieController()

@actors_in_movie_bp.route("/actors_in_movie", methods=['GET'])
def get_actors_in_movie():
    return actors_in_movie_controller.get_all()


@actors_in_movie_bp.route("/actors_in_movie/<int:actor_id>/<int:movie_id>", methods=['GET'])
def get_actors_in_movie_by_id(actor_id, movie_id):
    return actors_in_movie_controller.get_by_id((actor_id, movie_id))


@actors_in_movie_bp.route("/actors_in_movie/all", methods=['GET'])
def gel_all_actors_for_each_movie():
    return actors_in_movie_controller.get_actors_for_each_movie()

@actors_in_movie_bp.route("/actors_in_movie", methods=['POST'])
def add_actors_in_movie():
    return actors_in_movie_controller.create()

@actors_in_movie_bp.route("/actors_in_movie/<int:actor_id>/<int:movie_id>", methods=['PATCH'])
def update_actors_in_movie(actor_id, movie_id):
    return actors_in_movie_controller.update((actor_id, movie_id))

@actors_in_movie_bp.route("/actors_in_movie/<int:actor_id>/<int:movie_id>", methods=['DELETE'])
def delete_actors_in_movie(actor_id, movie_id):
    return actors_in_movie_controller.delete((actor_id, movie_id))
