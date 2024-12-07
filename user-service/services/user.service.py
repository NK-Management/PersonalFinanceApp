from flask import Blueprint, jsonify
from auth.jwt_handler import get_current_user

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/profile", methods=["GET"])
def profile():
    """
    Retrieves the profile of the current user.
    """
    user = get_current_user()
    return jsonify({"user_id": user["id"], "role": user["role"]}), 200

@user_blueprint.route("/admin/task", methods=["GET"])
def admin_task():
    """
    Executes an admin-specific task.
    """
    user = get_current_user()
    if user["role"] != "admin":
        return jsonify({"message": "Access denied"}), 403
    return jsonify({"message": "Admin-specific task executed!"}), 200

@user_blueprint.route("/user/task", methods=["GET"])
def user_task():
    """
    Executes a user-specific task.
    """
    user = get_current_user()
    return jsonify({"message": f"User-specific task executed for {user['id']}!"}), 200
