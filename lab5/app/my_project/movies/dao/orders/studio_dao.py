from ..general_dao import GeneralDAO
from my_project.database import db
from my_project.movies.dao.__init__ import Movie

class StudioDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Studio

    def __init__(self):
        super().__init__(self.Studio)

    def get_movies_by_studio_id(studio_id):
        movies = db.session.query(Movie).filter(Movie.studio_id == studio_id).all()
        return [movie.to_dict() for movie in movies]
