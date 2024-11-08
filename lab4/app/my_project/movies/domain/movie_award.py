from my_project.database import db
from sqlalchemy import ForeignKey


class MovieAward(db.Model):
    __tablename__ = "movie_award"

    award_id = db.Column(db.Integer, ForeignKey("award.id"), primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), primary_key=True)
    number = db.Column(db.Integer, nullable=True)

    movie = db.relationship("Movie", back_populates="award")
    award = db.relationship("Award", back_populates="movie")

    def to_dict(self):
        return {
            "award_id": self.award_id,
            "movie_id": self.movie_id,
            "number": self.number
        }
