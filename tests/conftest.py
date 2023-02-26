import pytest
from app import create_app, db
from app.models.car import Car
from app.models.owner import Owner
from flask_jwt_extended import create_access_token


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()

    with flask_app.app_context():
        db.create_all()

        # Create a test owner
        test_owner = Owner(name='John Doe')
        db.session.add(test_owner)
        db.session.commit()

        # Create test cars for the owner
        test_car_1 = Car(model='hatch', color='blue', owner_id=test_owner.id)
        test_car_2 = Car(model='sedan', color='gray', owner_id=test_owner.id)
        db.session.add(test_car_1)
        db.session.add(test_car_2)
        db.session.commit()

        # Create a test token for authentication
        test_token = create_access_token(identity=test_owner.id)

        yield testing_client, test_token

        db.session.remove()
        db.drop_all()