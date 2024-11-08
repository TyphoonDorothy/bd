from my_project.movies.dao.general_dao import GeneralDAO
from my_project.database import db
from my_project.movies.dao.__init__ import Movie

class DirectorDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Director
    
    def __init__(self):
        super().__init__(self.Director)


    def get_movies_by_director_id(director_id):
        movies = db.session.query(Movie).filter(Movie.director_id == director_id).all()
        return [movie.to_dict() for movie in movies]