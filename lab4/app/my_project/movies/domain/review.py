from my_project.database import db

class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(500), nullable=True)

    movs = db.relationship("Rating", back_populates="review")

    def to_dict(self):
        return {
            "id": self.id,
            "score": self.score,
            "review": self.review
        }
