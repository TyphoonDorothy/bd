from ..general_service import GeneralService
from my_project.movies.service.__init__ import ActorsInMovie, ActorsInMovieDAO
from my_project.database import db


class ActorsInMovieService(GeneralService):
    def __init__(self):
        super().__init__(ActorsInMovieDAO(), ActorsInMovie)
        self.model = ActorsInMovie

    def get_actors_for_each_movie(self):
        return self.dao.get_actors_for_each_movie()

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
