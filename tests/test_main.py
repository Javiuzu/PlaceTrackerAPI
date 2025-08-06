from fastapi.testclient import TestClient
from sqlalchemy.testing.pickleable import User

from app.database import SessionLocal
from app.main import get_db, app
from app import models

client = TestClient(app)


def test_create_user(client, db_session):
    user_data = {
        "username": "testUser",
        "email": "test@example.com",
        "password": "1234"
    }
    response = client.post("/signup",json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testUser"


def test_create_place(client, db_session):
    test_user = models.Users(username="Tester", email="tester@example.com")
    db_session.add(test_user)
    db_session.commit()
    db_session.refresh(test_user)

    # ✅ Now access test_user.id while session is active
    place_data = {
        "name": "Test Place",
        "country": "Test Country",
        "description": "Test Description",
        "visited": False,
        "user_id": test_user.id  # Make sure this is accessed BEFORE session closes
    }

    response = client.post("/places/", json=place_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Place"

def test_user_signup_and_login(client):
    # Create a new user
    signup_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpass"
    }
    response = client.post("/signup", json=signup_data)
    assert response.status_code == 200, response.text
    print("Signup response:", response.json())

    # Login with correct credentials
    login_data = {
        "username": "testuser",
        "password": "testpass"
    }
    response = client.post("/login", data=login_data)
    assert response.status_code == 200, response.text
    token_data = response.json()
    print("Login response:", token_data)

#TODO add more tests, check multiple user creation, same user creation, same email creation, etc.