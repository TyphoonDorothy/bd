from ..general_dao import GeneralDAO
from my_project.movies.dao.__init__ import Movie, Festival
from my_project.database import db

class MovieFestivalDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import MovieFestival

    def __init__(self):
        super().__init__(self.MovieFestival)


    def get_movies_for_each_festival(self):
        festivals = db.session.query(Festival).all()
        result = []

        for festival in festivals:
            movies = [association.movie.name for association in festival.movie]
            result.append({
                'festival': festival.name,
                'movies': movies
            })

        return result