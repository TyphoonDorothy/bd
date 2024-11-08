from ..general_dao import GeneralDAO
from my_project.database import db
from my_project.movies.dao.__init__ import Fact


class MovieDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Movie
    
    def __init__(self):
        super().__init__(self.Movie)


    def get_facts_by_movie_id(movie_id):
        facts = db.session.query(Fact).filter(Fact.movie_id == movie_id).all()
        return [fact.to_dict() for fact in facts]
