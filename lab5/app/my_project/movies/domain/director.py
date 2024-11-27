from my_project.database import db

class Director(db.Model):
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)

    movies = db.relationship("Movie", back_populates="director")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
        }
