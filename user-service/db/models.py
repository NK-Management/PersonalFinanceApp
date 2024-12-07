from db.db_setup import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserRole(db.Model):
    """
    Represents roles for users (e.g., admin, user, etc.).
    """
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)

class User(db.Model):
    """
    Represents a user in the system.
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("user_roles.id"), nullable=False)
    role = db.relationship("UserRole", backref="users")

    def set_password(self, password):
        """
        Sets the user's password hash.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifies the user's password.
        """
        return check_password_hash(self.password_hash, password)
