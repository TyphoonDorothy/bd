from my_project.database import db
from sqlalchemy import ForeignKey


class MovieGenre(db.Model):
    __tablename__ = "movie_genre"

    genre_id = db.Column(db.Integer, ForeignKey("genre.id"), primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), primary_key=True)

    movie = db.relationship("Movie", back_populates="genre")
    genre = db.relationship("Genre", back_populates="movie")

    def to_dict(self):
        return {
            "genre_id": self.genre_id,
            "movie_id": self.movie_id
        }
