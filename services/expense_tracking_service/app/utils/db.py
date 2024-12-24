from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


# Reflect users table dynamically
users = None  # Placeholder, will be set when app context is available

def reflect_users_table(app):
    global users
    with app.app_context():
        users = db.Table('users', db.metadata, autoload_with=db.engine, schema='public')