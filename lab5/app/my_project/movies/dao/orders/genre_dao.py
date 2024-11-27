from sqlalchemy import text
from ..general_dao import GeneralDAO
from my_project.database import db


class GenreDAO(GeneralDAO):
    from my_project.movies.dao.__init__ import Genre

    def __init__(self):
        super().__init__(self.Genre)

    def insert_genre(self, name):
        query = text("INSERT INTO genre (name) VALUES (:name)")
        result = db.session.execute(query, {"name": name})
        db.session.commit()
        return result.lastrowid
