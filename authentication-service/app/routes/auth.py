from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User, db
from app.utils.decorators import role_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return {"message": "User with this email already exists"}, 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return {"message": "Invalid credentials"}, 401

    access_token = create_access_token(identity=user.id)
    return {"access_token": access_token}, 200

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404

    return {"username": user.username, "email": user.email, "role": user.role}, 200

@auth_bp.route("/role/<int:user_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_role(user_id):
    data = request.get_json()
    new_role = data.get("role")

    if new_role not in ["user", "admin"]:
        return {"message": "Invalid role"}, 400

    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404

    user.role = new_role
    db.session.commit()
    return {"message": f"User role updated to {new_role}"}, 200
