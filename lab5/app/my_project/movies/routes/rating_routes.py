from flask import Blueprint, jsonify
from my_project.movies.controller.orders.rating_controller import RatingController

rating_bp = Blueprint("ratings", __name__)
rating_controller = RatingController()

@rating_bp.route("/ratings", methods=['GET'])
def get_ratings():
    return rating_controller.get_all()

@rating_bp.route("/ratings/<int:review_id>/<int:movie_id>", methods=['GET'])
def get_rating_by_id(review_id, movie_id):
    return rating_controller.get_by_id((review_id, movie_id))

@rating_bp.route("/ratings", methods=['POST'])
def add_rating():
    return rating_controller.create()

@rating_bp.route("/ratings/<int:review_id>/<int:movie_id>", methods=['PATCH'])
def update_rating(review_id, movie_id):
    return rating_controller.update((review_id, movie_id))

@rating_bp.route("/ratings/<int:review_id>/<int:movie_id>", methods=['DELETE'])
def delete_rating(review_id, movie_id):
    return rating_controller.delete((review_id, movie_id))
