from my_project.database import db


class Genre(db.Model):
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    movie = db.relationship("MovieGenre", back_populates="genre")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
