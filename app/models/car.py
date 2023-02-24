from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __repr__(self):
        return f'<Car {self.color} {self.model}>'

    def to_dict(self):
        return {
            'id': self.id,
            'color': self.color,
            'model': self.model,
            'owner_id': self.owner_id
        }