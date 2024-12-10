from flask import Blueprint, request, jsonify
from user_service.db.models import User, UserRole
from user_service.db.db_setup import db
from user_service.services.auth.jwt_handler import generate_token, get_current_user
from user_service.services.cache.cache_handler import cache_token, invalidate_token

auth_blueprint = Blueprint("auth", __name__)

def admin_required(func):
    """
    Decorator to ensure the current user is an admin.
    """
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if user["role"] != "admin":
            return jsonify({"message": "Access denied. Admin role required."}), 403
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@auth_blueprint.route("/register", methods=["POST"])
def register():
    """
    Registers a new user. Role defaults to 'user'.
    Only admins can set custom roles.
    """
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role_name = "user"  # Default role is always "user"

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User with this email already exists."}), 400

    # Validate the role (role_name is always "user" here unless admin explicitly sets it)
    role = UserRole.query.filter_by(role_name=role_name).first()  # "user" role must exist
    if not role:
        return jsonify({"message": f"Role '{role_name}' does not exist."}), 400

    # Create user with default role "user"
    new_user = User(username=username, email=email, role_id=role.id)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Generate JWT token for the newly registered user
    token = generate_token(new_user)

    # Cache the token for future invalidation if necessary
    cache_token(new_user.id, token)

    return jsonify({"message": f"User registered successfully with role '{role_name}'.", "token": token}), 201

@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Logs in a user and generates a token.
    """
    data = request.json
    email, password = data["email"], data["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Generate JWT token for the user
    token = generate_token(user)
    
    # Cache the token for future invalidation
    cache_token(user.id, token)

    return jsonify({"token": token, "role": user.role.role_name}), 200

@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    """
    Logs out a user and invalidates their token.
    """
    user = get_current_user()
    invalidate_token(user["id"])  # Invalidate the token by removing it from the cache
    
    return jsonify({"message": "Logged out successfully"}), 200

@auth_blueprint.route("/create_role", methods=["POST"])
@admin_required
def create_role():
    """
    Allows admins to create new roles.
    """
    data = request.json
    role_name = data.get("role_name")

    if not role_name:
        return jsonify({"message": "Role name is required."}), 400

    if UserRole.query.filter_by(role_name=role_name).first():
        return jsonify({"message": f"Role '{role_name}' already exists."}), 400

    # Create a new role
    new_role = UserRole(role_name=role_name)
    db.session.add(new_role)
    db.session.commit()

    return jsonify({"message": f"Role '{role_name}' created successfully."}), 201
