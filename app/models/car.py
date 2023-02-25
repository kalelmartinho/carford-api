from app import db

class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum("yellow", "blue", "gray"), nullable=False)
    model = db.Column(db.Enum("hatch", "sedan", "convertible"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)
    owner = db.relationship("Owner", backref=db.backref("cars", lazy=True))

    def __repr__(self):
        return f"<Car {self.color} {self.model}>"