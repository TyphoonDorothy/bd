from my_project.database import db
from sqlalchemy import ForeignKey


class Rating(db.Model):
    __tablename__ = "rating"

    review_id = db.Column(db.Integer, ForeignKey("review.id"), primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), primary_key=True)

    movie = db.relationship("Movie", back_populates="ratings")
    review = db.relationship("Review", back_populates="movs")

    def to_dict(self):
        return {
            "review_id": self.review_id,
            "movie_id": self.movie_id
        }
