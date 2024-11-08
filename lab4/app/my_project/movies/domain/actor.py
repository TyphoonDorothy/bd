from my_project.database import db

class Actor(db.Model):
    __tablename__ = "actor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    # Setting up a consistent relationship with ActorsInMovie
    movies = db.relationship("ActorsInMovie", back_populates="actor")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birthday": self.birthday
        }
