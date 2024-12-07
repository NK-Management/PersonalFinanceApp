from flask_caching import Cache
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

cache = Cache()

def init_cache(app):
    cache.init_app(app)

def generate_token(user):
    return create_access_token(identity={"id": user.id, "role": user.role.role_name})

@jwt_required()
def get_current_user():
    return get_jwt_identity()
