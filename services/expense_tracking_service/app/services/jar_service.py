from services.expense_tracking_service.app import db
from services.expense_tracking_service.app.models.jar import Jar
from services.expense_tracking_service.app.schemas.jar_schema import JarSchema
from services.expense_tracking_service.app.utils.jwt_handler import decode_jwt
from flask import request

class JarService:
    @staticmethod
    def create_jar(data):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Create a jar associated with the logged-in user
        jar = Jar(name=data['name'], category=data['category'], balance=data['balance'], user_id=user_id)
        db.session.add(jar)
        db.session.commit()
        return JarSchema().dump(jar)

    @staticmethod
    def get_all_jars():
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch only the logged-in user's jars
        jars = Jar.query.filter_by(user_id=user_id).all()
        return JarSchema(many=True).dump(jars)

    @staticmethod
    def get_jar_by_id(jar_id):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch the jar only if it belongs to the logged-in user
        jar = Jar.query.filter_by(id=jar_id, user_id=user_id).first()
        if jar:
            return JarSchema().dump(jar)
        return None

    @staticmethod
    def update_jar(jar_id, data):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Update the jar only if it belongs to the logged-in user
        jar = Jar.query.filter_by(id=jar_id, user_id=user_id).first()
        if jar:
            jar.name = data['name']
            jar.category = data['category']
            jar.balance = data['balance']
            db.session.commit()
            return JarSchema().dump(jar)
        return None

    @staticmethod
    def delete_jar(jar_id):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Delete the jar only if it belongs to the logged-in user
        jar = Jar.query.filter_by(id=jar_id, user_id=user_id).first()
        if jar:
            db.session.delete(jar)
            db.session.commit()
            return {'message': 'Jar deleted successfully'}
        return {'message': 'Jar not found'}
