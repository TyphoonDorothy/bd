from my_project.movies.service.general_service import GeneralService
from my_project.movies.service.__init__ import Actor
from my_project.movies.service.__init__ import ActorDAO
from my_project.database import db

class ActorService(GeneralService):
    def __init__(self):
        super().__init__(ActorDAO(), Actor)
        self.model = Actor

        def delete(self, entity_id):
            entity = db.session.query(self.model).get(entity_id)
            if entity:
                db.session.delete(entity)
                db.session.commit()
                return True
            return False