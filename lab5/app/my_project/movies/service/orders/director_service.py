from my_project.movies.service.general_service import GeneralService
from my_project.movies.service.__init__ import Director, DirectorDAO
from my_project.database import db


class DirectorService(GeneralService):
    def __init__(self):
        super().__init__(DirectorDAO(), Director)
        self.model = Director


    def get_movies_by_director_id(self, director_id):
        return DirectorDAO.get_movies_by_director_id(director_id)

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
