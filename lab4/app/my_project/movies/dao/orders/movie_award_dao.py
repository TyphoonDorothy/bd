from ..general_dao import GeneralDAO
from my_project.movies.dao.__init__ import Movie, Award
from my_project.database import db


class MovieAwardDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import MovieAward

    def __init__(self):
        super().__init__(self.MovieAward)


    def get_movies_for_each_award(self):
        awards = db.session.query(Award).all()
        result = []

        for award in awards:
            movies = [association.movie.name for association in award.movie]
            result.append({
                'award': award.name,
                'movies': movies
            })

        return result