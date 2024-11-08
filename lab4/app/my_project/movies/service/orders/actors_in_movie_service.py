from ..general_service import GeneralService
from my_project.movies.service.__init__ import ActorsInMovie, ActorsInMovieDAO


class ActorsInMovieService(GeneralService):
    def __init__(self):
        super().__init__(ActorsInMovieDAO(), ActorsInMovie)

    def get_actors_for_each_movie(self):
        return self.dao.get_actors_for_each_movie()
