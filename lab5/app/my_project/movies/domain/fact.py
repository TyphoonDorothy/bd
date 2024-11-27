from my_project.database import db
from sqlalchemy import ForeignKey


class Fact(db.Model):
    __tablename__ = "fact"

    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(500), nullable=False)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), nullable=False)

    movie = db.relationship("Movie", back_populates="facts")

    def to_dict(self):
        return {
            "id": self.id,
            "fact": self.fact,
            "movie_id": self.movie_id
        }
