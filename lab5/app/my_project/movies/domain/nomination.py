from my_project.database import db


class Nomination(db.Model):
    __tablename__ = "nomination"

    id = db.Column(db.Integer, primary_key=True)
    award_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "award_id": self.award_id,
            "id": self.id,
            "name": self.name,
        }
