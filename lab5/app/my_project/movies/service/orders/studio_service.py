from ..general_service import GeneralService
from my_project.movies.service.__init__ import Studio, StudioDAO
from my_project.database import db


class StudioService(GeneralService):
    def __init__(self):
        super().__init__(StudioDAO(), Studio)
        self.model = Studio

    def get_movies_by_studio_id(self, studio_id):
        return StudioDAO.get_movies_by_studio_id(studio_id)

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
