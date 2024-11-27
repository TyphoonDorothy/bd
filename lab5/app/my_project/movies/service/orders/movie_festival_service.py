from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieFestival, MovieFestivalDAO
from my_project.database import db


class MovieFestivalService(GeneralService):
    def __init__(self):
        super().__init__(MovieFestivalDAO(), MovieFestival)
        self.model = MovieFestival

    def get_movies_for_each_festival(self):
        return self.dao.get_movies_for_each_festival()

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False