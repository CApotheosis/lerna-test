from project import db


class Cats(db.Model):
    __tablename__ = "cats"

    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String(50), index=True, nullable=False)
    name = db.Column(db.String(50), index=True, nullable=False)
    age_by_month = db.Column(db.Integer, index=True, nullable=False)
    description = db.Column(db.String(250), index=True, nullable=False)

    def __repr__(self):
        return f"{self.name.capitalize()} of {self.breed} breed."
