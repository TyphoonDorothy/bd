from ..general_dao import GeneralDAO
from my_project.movies.dao.__init__ import Movie, Actor
from my_project.database import db


class ActorsInMovieDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import ActorsInMovie

    def __init__(self):
        super().__init__(self.ActorsInMovie)

    def get_actors_for_each_movie(self):
        movies = db.session.query(Movie).all()
        result = []

        for movie in movies:
            # Accessing actors through the association table
            actors = [association.actor.name for association in movie.actors]
            result.append({
                'movie': movie.name,
                'actors': actors
            })

        return result
