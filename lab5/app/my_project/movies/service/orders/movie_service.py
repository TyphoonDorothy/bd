from ..general_service import GeneralService
from my_project.movies.service.__init__ import Movie, MovieDAO
from my_project.database import db


class MovieService(GeneralService):
    def __init__(self):
        super().__init__(MovieDAO(), Movie)
        self.model = Movie


    def get_facts_by_movie_id(self, movie_id):
        return MovieDAO.get_facts_by_movie_id(movie_id)

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

