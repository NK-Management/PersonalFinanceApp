from flask import Flask
from user_service.config import Config
from user_service.db.db_setup import init_db
from user_service.services.cache.cache_handler import init_cache
from flask_jwt_extended import JWTManager
from user_service.services.auth.auth_service import auth_blueprint
from user_service.services.user_route_service import user_blueprint


def create_app(Config_class=Config):
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config_class)

    # Initialize extensions
    init_db(app)
    init_cache(app)
    jwt = JWTManager(app)

    # Register blueprints

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(user_blueprint, url_prefix="/user"   )

    return app