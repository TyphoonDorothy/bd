from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieGenre, MovieGenreDAO


class MovieGenreService(GeneralService):
    def __init__(self):
        super().__init__(MovieGenreDAO(), MovieGenre)

    def get_movies_for_each_genre(self):
        return self.dao.get_movies_for_each_genre()