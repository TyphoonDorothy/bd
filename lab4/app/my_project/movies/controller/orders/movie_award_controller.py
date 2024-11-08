from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import MovieAwardService
from flask import jsonify


class MovieAwardController(GeneralController):
    def __init__(self):
        super().__init__(MovieAwardService())


    def get_movies_for_each_award(self):
        data = self.service.get_movies_for_each_award()
        return jsonify(data)
