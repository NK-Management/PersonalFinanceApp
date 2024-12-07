from flask import Flask
from config import Config
from db.db_setup import init_db
from cache.cache_handler import init_cache
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize extensions
    init_db(app)
    init_cache(app)
    jwt = JWTManager(app)

    # Register blueprints
    from auth.auth_service import auth_blueprint
    from services.user_service import user_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(user_blueprint, url_prefix="/user"   )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
