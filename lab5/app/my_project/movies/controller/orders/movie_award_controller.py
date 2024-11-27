from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import MovieAwardService
from flask import jsonify


class MovieAwardController(GeneralController):
    def __init__(self):
        super().__init__(MovieAwardService())

    def get_movies_for_each_award(self):
        data = self.service.get_movies_for_each_award()
        return jsonify(data)

    def add_movie_award(self, request_data):
        award_id = request_data.get("award_id")
        movie_id = request_data.get("movie_id")
        number = request_data.get("number", None)
        if not award_id or not movie_id:
            return jsonify({"error": "award_id and movie_id are required"}), 400
        response = self.service.add_movie_award(award_id, movie_id, number)
        return jsonify(response), 201