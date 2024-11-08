from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieAward, MovieAwardDAO


class MovieAwardService(GeneralService):
    def __init__(self):
        super().__init__(MovieAwardDAO(), MovieAward)

    def get_movies_for_each_award(self):
        return self.dao.get_movies_for_each_award()