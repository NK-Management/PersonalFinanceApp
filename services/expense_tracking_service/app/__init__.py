from flask import Flask
from flask_marshmallow import Marshmallow
from services.expense_tracking_service.app.config import Config
from services.expense_tracking_service.app.utils.db import db
from flask_cors import CORS


ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    CORS(app)
    app.config.from_object(Config)
    # print(app.config)

    ma.init_app(app)
    # Initialize plugins
    db.init_app(app)
    # print("SQLAlchemy initialized:", db)

    # # Check if SQLAlchemy is in the app extensions
    # print("SQLAlchemy in app.extensions:", app.extensions.get('sqlalchemy'))

    # Register blueprints (routes)
    from services.expense_tracking_service.app.routes.jars import bp as jars_bp
    from services.expense_tracking_service.app.routes.expenses import bp as expenses_bp
    from services.expense_tracking_service.app.routes.incomes import bp as incomes_bp
    from services.expense_tracking_service.app.routes.goals import bp as goals_bp

    app.register_blueprint(jars_bp, url_prefix='/jars')
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    app.register_blueprint(incomes_bp, url_prefix='/incomes')
    app.register_blueprint(goals_bp, url_prefix='/goals')

    return app
