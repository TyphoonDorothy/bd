from flask import Blueprint, jsonify, request
from my_project.database import db
from ..controller.orders.movie_controller import ReviewController
from ..domain.actor import Actor
from ..domain.movie import Movie

movie_bp = Blueprint("movies", __name__)
movie_controller = ReviewController()


@movie_bp.route("/movies", methods=['GET'])
def get_movies():
    return movie_controller.get_all()

@movie_bp.route("/movies/<int:movie_id>", methods=['GET'])
def get_movie_by_id(movie_id):
    return movie_controller.get_by_id(movie_id)

@movie_bp.route("/movies/<int:movie_id>/facts", methods=['GET'])
def get_facts_by_movie(movie_id):
    return jsonify(movie_controller.service.get_facts_by_movie_id(movie_id))

@movie_bp.route("/movies", methods=['POST'])
def add_movie():
    return movie_controller.create()

@movie_bp.route("/movies/<int:movie_id>", methods=['PATCH'])
def update_movie(movie_id):
    return movie_controller.update(movie_id)

@movie_bp.route("/movies/<int:movie_id>", methods=['DELETE'])
def delete_movie(movie_id):
    return movie_controller.delete(movie_id)

@movie_bp.route('/api/movies/<int:movie_id>/actors', methods=['PUT'])
def update_movie_actors(movie_id):
    actor_ids = request.json.get('actor_ids', [])
    movie = Movie.query.get_or_404(movie_id)
    actors = Actor.query.filter(Actor.id.in_(actor_ids)).all()
    movie.actors = actors
    db.session.commit()

    return jsonify({
        "message": "Actors updated successfully",
        "movie_id": movie.id,
        "actor_ids": [actor.id for actor in actors]
    }), 200
