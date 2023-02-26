from app import db

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    has_car = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Owner {self.name}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'has_car': self.has_car}