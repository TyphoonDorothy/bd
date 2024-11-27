from ..general_service import GeneralService
from my_project.movies.service.__init__ import Award, AwardDAO
from my_project.database import db


class AwardService(GeneralService):
    def __init__(self):
        super().__init__(AwardDAO(), Award)
        self.model = Award

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
