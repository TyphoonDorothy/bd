from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import MovieGenreService
from flask import jsonify


class MovieAwardController(GeneralController):
    def __init__(self):
        super().__init__(MovieGenreService())


    def get_movies_for_each_genre(self):
        data = self.service.get_movies_for_each_genre()
        return jsonify(data)
