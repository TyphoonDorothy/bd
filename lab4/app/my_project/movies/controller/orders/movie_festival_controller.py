from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import MovieFestivalService
from flask import jsonify


class MovieFestivalController(GeneralController):
    def __init__(self):
        super().__init__(MovieFestivalService())


    def get_movies_for_each_festival(self):
        data = self.service.get_movies_for_each_festival()
        return jsonify(data)
