from ..general_service import GeneralService
from my_project.movies.service.__init__ import Review, ReviewDAO
from my_project.database import db
from sqlalchemy import text


class ReviewService(GeneralService):
    def __init__(self):
        super().__init__(ReviewDAO(), Review)
        self.model = Review

    def calculate_score(self, calculation_type):
        query = text("SELECT calc_score(:type) AS score")
        result = db.session.execute(query, {"type": calculation_type}).fetchone()

        if result:
            return result[0]
        else:
            raise ValueError("Error retrieving calculation result")

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
