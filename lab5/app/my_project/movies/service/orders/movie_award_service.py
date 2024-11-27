from ..general_service import GeneralService
from my_project.movies.service.__init__ import MovieAward, MovieAwardDAO
from my_project.database import db


class MovieAwardService(GeneralService):
    def __init__(self):
        super().__init__(MovieAwardDAO(), MovieAward)
        self.model = MovieAward

    def get_movies_for_each_award(self):
        return self.dao.get_movies_for_each_award()

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def add_movie_award(self, award_id, movie_id, number=None):
        self.dao.insert_movie_award(award_id, movie_id, number)
        return {"message": "Movie-Award association added successfully"}