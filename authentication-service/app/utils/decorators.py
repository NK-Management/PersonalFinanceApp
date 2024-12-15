from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from functools import wraps
from app.models.user import User

def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if user and user.role == required_role:
                return fn(*args, **kwargs)
            return {"message": "Access forbidden: Admins only"}, 403
        return decorator
    return wrapper
