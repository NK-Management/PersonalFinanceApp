from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.schemas.user_schema import UserSchema
from app.utils.decorators import role_required

auth_bp = Blueprint("auth", __name__)

# Schema instances for validation and serialization
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user.
    """
    try:
        # Validate incoming data
        data = user_schema.load(request.json)

        # Create a new user using the service
        new_user = UserService.create_user(data)
        return {"message": "User registered successfully", "user": user_schema.dump(new_user)}, 201

    except ValueError as ve:
        return {"message": str(ve)}, 400
    except Exception as e:
        return {"message": "An error occurred while registering the user", "error": str(e)}, 500


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user and return a JWT token.
    """
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

        user = UserService.get_user_by_email(email)
        if not user or not user.check_password(password):
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200

    except Exception as e:
        return {"message": "An error occurred while logging in", "error": str(e)}, 500


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    """
    Get details of the currently authenticated user.
    """
    try:
        user_id = get_jwt_identity()
        user = UserService.get_user_by_id(user_id)

        if not user:
            return {"message": "User not found"}, 404

        return {"user": user_schema.dump(user)}, 200

    except Exception as e:
        return {"message": "An error occurred while fetching user data", "error": str(e)}, 500


@auth_bp.route("/role/<int:user_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_role(user_id):
    """
    Update the role of a user (Admin only).
    """
    try:
        data = request.json
        new_role = data.get("role")

        if new_role not in ["user", "admin"]:
            return {"message": "Invalid role"}, 400

        updated_user = UserService.update_user_role(user_id, new_role)
        return {
            "message": f"User role updated to {new_role}",
            "user": user_schema.dump(updated_user),
        }, 200

    except ValueError as ve:
        return {"message": str(ve)}, 404
    except Exception as e:
        return {"message": "An error occurred while updating the role", "error": str(e)}, 500
