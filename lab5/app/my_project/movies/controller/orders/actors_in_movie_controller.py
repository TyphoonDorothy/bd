from ..general_controller import GeneralController
from my_project.movies.controller.__init__ import ActorsInMovieService
from flask import jsonify


class ActorsInMovieController(GeneralController):
    def __init__(self):
        super().__init__(ActorsInMovieService())

    def get_actors_for_each_movie(self):
        data = self.service.get_actors_for_each_movie()
        return jsonify(data)
