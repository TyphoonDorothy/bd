from my_project.database import db
from sqlalchemy import ForeignKey


class Movie(db.Model):
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Date, nullable=False)
    director_id = db.Column(db.Integer, ForeignKey("director.id"), nullable=False)
    studio_id = db.Column(db.Integer, ForeignKey("studio.id"), nullable=False)

    studio = db.relationship("Studio", back_populates="movies")
    director = db.relationship("Director", back_populates="movies")
    facts = db.relationship("Fact", back_populates="movie")
    ratings = db.relationship("Rating", back_populates="movie")
    actors = db.relationship("ActorsInMovie", back_populates="movie")
    genre = db.relationship("MovieGenre", back_populates="movie")
    festival = db.relationship("MovieFestival", back_populates="movie")
    award = db.relationship("MovieAward", back_populates="movie")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "director_id": self.director_id,
            "studio_id": self.studio_id,
        }
