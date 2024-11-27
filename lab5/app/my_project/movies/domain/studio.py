from my_project.database import db

class Studio(db.Model):
    __tablename__ = "studio"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)

    movies = db.relationship("Movie", back_populates="studio")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country
        }
