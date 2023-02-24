from app import db

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    cars = db.relationship('Car', backref='owner', lazy=True)

    def __repr__(self):
        return f'<Owner {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'cars': [car.to_dict() for car in self.cars]
        }