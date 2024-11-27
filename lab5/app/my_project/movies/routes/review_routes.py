from flask import Blueprint
from ..controller.orders.review_controller import ReviewController


review_bp = Blueprint("reviews", __name__)
review_controller = ReviewController()

@review_bp.route("/reviews", methods=['GET'])
def get_reviews():
    return review_controller.get_all()

@review_bp.route("/reviews/<int:review_id>", methods=['GET'])
def get_review_by_id(review_id):
    return review_controller.get_by_id(review_id)

@review_bp.route("/reviews", methods=['POST'])
def add_review():
    return review_controller.create()

@review_bp.route("/reviews/<int:review_id>", methods=['PATCH'])
def update_review(review_id):
    return review_controller.update(review_id)

@review_bp.route("/reviews/<int:review_id>", methods=['DELETE'])
def delete_review(review_id):
    return review_controller.delete(review_id)

@review_bp.route("/reviews/calculate", methods=['GET'])
def calculate_score():
    return review_controller.calculate_score()