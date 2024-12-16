import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    """
    Set up a test client for the application.
    Initializes an in-memory SQLite database for testing.
    """
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["JWT_SECRET_KEY"] = "testsecretkey"  # Ensure a consistent secret key for testing
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Seed admin user
            admin = User(username="admin", email="admin@example.com", role="admin")
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
        yield client


def test_register(client):
    """
    Test user registration endpoint.
    """
    response = client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data["message"] == "User registered successfully"

    # Validate the user was created in the database
    with client.application.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        assert user is not None
        assert user.username == "testuser"


def test_login(client):
    """
    Test user login endpoint.
    """
    response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    assert response.status_code == 200
    response_data = response.get_json()
    assert "access_token" in response_data


def test_get_current_user(client):
    """
    Test retrieving the current authenticated user's information.
    """
    # Authenticate to get access token
    login_response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    token = login_response.get_json()["access_token"]

    # Use the token to access the protected route
    response = client.get("/api/auth/me", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data["username"] == "admin"
    assert response_data["email"] == "admin@example.com"
    assert response_data["role"] == "admin"


def test_update_role(client):
    """
    Test updating a user's role (admin-only endpoint).
    """
    # Authenticate as admin to get access token
    login_response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    token = login_response.get_json()["access_token"]

    # Create a test user
    with client.application.app_context():
        test_user = User(username="testuser", email="testuser@example.com", role="user")
        test_user.set_password("password123")
        db.session.add(test_user)
        db.session.commit()

    # Update the role of the test user
    response = client.put(f"/api/auth/role/{test_user.id}", 
        json={"role": "admin"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data["message"] == "User role updated to admin"

    # Validate the role change in the database
    with client.application.app_context():
        updated_user = User.query.get(test_user.id)
        assert updated_user.role == "admin"
