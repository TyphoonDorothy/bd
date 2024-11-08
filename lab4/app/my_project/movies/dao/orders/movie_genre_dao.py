from ..general_dao import GeneralDAO
from my_project.movies.dao.__init__ import Movie, Genre
from my_project.database import db


class MovieGenreDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import MovieGenre

    def __init__(self):
        super().__init__(self.MovieGenre)


    def get_movies_for_each_genre(self):
        genres = db.session.query(Genre).all()
        result = []

        for genre in genres:
            movies = [association.movie.name for association in genre.movie]
            result.append({
                'genre': genre.name,
                'movies': movies
            })

        return result
