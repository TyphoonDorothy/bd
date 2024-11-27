from ..general_service import GeneralService
from my_project.movies.service.__init__ import Genre, GenreDAO
from sqlalchemy import text
from my_project.database import db


class GenreService(GeneralService):
    def __init__(self):
        super().__init__(GenreDAO(), Genre)
        self.model = Genre

    def create_genre(self, name):
        return self.dao.insert_genre(name)

    def insert_genres(self):
        query = text("CALL insert_genres()")
        db.session.execute(query)
        db.session.commit()
