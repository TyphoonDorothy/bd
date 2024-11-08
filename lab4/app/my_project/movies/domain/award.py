from my_project.database import db


class Award(db.Model):
    __tablename__ = "award"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    movie = db.relationship("MovieAward", back_populates="award")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
