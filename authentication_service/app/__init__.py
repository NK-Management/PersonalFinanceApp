from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    CORS(app)
    app.config.from_object("authentication_service.app.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    # Import inside function to avoid circular dependency
    from authentication_service.app.routes.auth import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
