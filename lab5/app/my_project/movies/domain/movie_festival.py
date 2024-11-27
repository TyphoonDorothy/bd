from my_project.database import db
from sqlalchemy import ForeignKey


class MovieFestival(db.Model):
    __tablename__ = "movie_festival"

    festival_id = db.Column(db.Integer, ForeignKey("festival.id"), primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), primary_key=True)

    movie = db.relationship("Movie", back_populates="festival")
    festival = db.relationship("Festival", back_populates="movie")

    def to_dict(self):
        return {
            "festival_id": self.festival_id,
            "movie_id": self.movie_id
        }
