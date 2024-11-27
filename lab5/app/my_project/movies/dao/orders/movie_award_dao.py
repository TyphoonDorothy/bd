from ..general_dao import GeneralDAO
from my_project.movies.dao.__init__ import Award
from my_project.database import db
from sqlalchemy import text

class MovieAwardDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import MovieAward

    def __init__(self):
        super().__init__(self.MovieAward)

    def insert_movie_award(self, award_id, movie_id, number=None):
        query = text("""
            INSERT INTO movie_award (award_id, movie_id, number)
            VALUES (:award_id, :movie_id, :number)
        """)
        db.session.execute(query, {"award_id": award_id, "movie_id": movie_id, "number": number})
        db.session.commit()

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