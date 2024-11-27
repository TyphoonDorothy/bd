from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieGenre, MovieGenreDAO
from my_project.database import db


class MovieGenreService(GeneralService):
    def __init__(self):
        super().__init__(MovieGenreDAO(), MovieGenre)
        self.model = MovieGenre

    def get_movies_for_each_genre(self):
        return self.dao.get_movies_for_each_genre()

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False