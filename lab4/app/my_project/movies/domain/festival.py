from my_project.database import db


class Festival(db.Model):
    __tablename__ = "festival"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(50), nullable=False)

    movie = db.relationship("MovieFestival", back_populates="festival")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place
        }
