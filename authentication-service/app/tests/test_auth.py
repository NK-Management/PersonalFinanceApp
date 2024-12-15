import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
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
    response = client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "User registered successfully"

def test_login(client):
    response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_get_current_user(client):
    login_response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    token = login_response.get_json()["access_token"]

    response = client.get("/api/auth/me", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.get_json()["username"] == "admin"

def test_update_role(client):
    login_response = client.post("/api/auth/login", json={
        "email": "admin@example.com",
        "password": "admin123"
    })
    token = login_response.get_json()["access_token"]

    # Create a test user
    test_user = User(username="testuser", email="testuser@example.com", role="user")
    test_user.set_password("password123")
    db.session.add(test_user)
    db.session.commit()

    response = client.put(f"/api/auth/role/{test_user.id}", 
        json={"role": "admin"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.get_json()["message"] == "User role updated to admin"
