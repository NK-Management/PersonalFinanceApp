import pytest
from user_service.app import create_app
from user_service.db.db_setup import db
from user_service.db.models import User, UserRole
import os
from dotenv import load_dotenv

@pytest.fixture
def client():
    # Setup the app and test client
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///default.db")  # Use an in-memory DB for testing
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            # Create all tables
            db.create_all()
        yield client

    # Teardown - Drop all tables
    with app.app_context():
        db.drop_all()

def test_register(client):
    """
    Test the /register endpoint for user registration
    """
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }

    response = client.post('/register', json=data)
    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully with role 'user'."

def test_login(client):
    """
    Test the /login endpoint
    """
    data = {
        "email": "testuser@example.com",
        "password": "password123"
    }

    # Register the user first
    client.post('/register', json=data)

    response = client.post('/login', json=data)
    assert response.status_code == 200
    assert "token" in response.json
    assert "role" in response.json

def test_create_role(client):
    """
    Test the /create_role endpoint (admin only)
    """
    data = {
        "role_name": "admin"
    }

    # First login as an admin user (you can modify the user creation to assign admin role)
    client.post('/register', json={"username": "admin", "email": "admin@example.com", "password": "admin123", "role": "admin"})

    response = client.post('/create_role', json=data)
    assert response.status_code == 201
    assert response.json["message"] == "Role 'admin' created successfully."

def test_login_invalid_credentials(client):
    """
    Test login with invalid credentials
    """
    data = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }

    response = client.post('/login', json=data)
    assert response.status_code == 401
    assert response.json["message"] == "Invalid credentials"
