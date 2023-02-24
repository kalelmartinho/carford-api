from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import owner, car
    app.register_blueprint(owner.owner_bp)
    app.register_blueprint(car.car_bp)

    return app


from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()