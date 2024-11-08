from my_project.database import db
from sqlalchemy import ForeignKey

class ActorsInMovie(db.Model):
    __tablename__ = "actors_in_movie"

    actor_id = db.Column(db.Integer, ForeignKey("actor.id"), primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey("movie.id"), primary_key=True)

    movie = db.relationship("Movie", back_populates="actors")
    actor = db.relationship("Actor", back_populates="movies")

    def to_dict(self):
        return {
            "actor_id": self.actor_id,
            "movie_id": self.movie_id
        }
