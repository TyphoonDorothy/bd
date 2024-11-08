from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieFestival, MovieFestivalDAO


class MovieFestivalService(GeneralService):
    def __init__(self):
        super().__init__(MovieFestivalDAO(), MovieFestival)


    def get_movies_for_each_festival(self):
        return self.dao.get_movies_for_each_festival()