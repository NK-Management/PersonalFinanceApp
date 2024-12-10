import pytest
from user_service.app import create_app
from user_service.db.db_setup import db
from user_service.db.models import User, UserRole
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture
def client():
    """
    Set up Flask testing client with an existing database.
    Modifies only test-specific data without affecting other data.
    """
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///default.db")  # Use your actual DB URL here
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            # Rollback any uncommitted transactions to ensure no uncommitted changes pollute the database
            db.session.rollback()
        yield client

        # Teardown: Remove test-specific data
        with app.app_context():
            # Delete only the test data that was inserted by the test functions.
            # If you want to delete only specific entries, use more precise queries.
            db.session.query(User).filter(User.email.startswith('testuser')).delete()  # Example: deleting test users
            db.session.query(UserRole).filter(UserRole.role_name.startswith('testrole')).delete()  # Delete test roles if any
            db.session.commit()

def test_register(client):
    """
    Test the /auth/register endpoint for user registration
    """
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }

    response = client.post('/auth/register', json=data)
    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully with role 'user'."

def test_login(client):
    """
    Test the /auth/login endpoint
    """
    # Register the user first
    client.post('/auth/register', json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    })

    data = {
        "email": "testuser@example.com",
        "password": "password123"
    }

    response = client.post('/auth/login', json=data)
    assert response.status_code == 200
    assert "token" in response.json
    assert "role" in response.json

def test_create_role(client):
    """
    Test the /auth/create_role endpoint (admin only)
    """
    # Register an admin user and simulate login to get the token
    admin_data = {
        "username": "admin",
        "email": "admin@example.com",
        "password": "admin123",
        "role": "admin"
    }
    client.post('/auth/register', json=admin_data)
    login_response = client.post('/auth/login', json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    token = login_response.json.get("token")

    # Set the authorization header for the admin user
    headers = {"Authorization": f"Bearer {token}"}
    role_data = {"role_name": "admin"}

    response = client.post('/auth/create_role', json=role_data, headers=headers)
    assert response.status_code == 201
    assert response.json["message"] == "Role 'admin' created successfully."

def test_login_invalid_credentials(client):
    """
    Test /auth/login with invalid credentials
    """
    data = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }

    response = client.post('/auth/login', json=data)
    assert response.status_code == 401
    assert response.json["message"] == "Invalid credentials"
