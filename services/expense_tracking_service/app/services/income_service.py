from flask import request
from services.expense_tracking_service.app import db
from services.expense_tracking_service.app.models.income import Income
from services.expense_tracking_service.app.schemas.income_schema import IncomeSchema
from services.expense_tracking_service.app.utils.jwt_handler import decode_jwt

class IncomeService:
    @staticmethod
    def create_income(data):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Create an income record associated with the logged-in user
        income = Income(amount=data['amount'], description=data['description'], user_id=user_id)
        db.session.add(income)
        db.session.commit()
        return IncomeSchema().dump(income)

    @staticmethod
    def get_all_incomes():
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch only the logged-in user's incomes
        incomes = Income.query.filter_by(user_id=user_id).all()
        return IncomeSchema(many=True).dump(incomes)

    @staticmethod
    def get_income_by_id(income_id):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch the income only if it belongs to the logged-in user
        income = Income.query.filter_by(id=income_id, user_id=user_id).first()
        if income:
            return IncomeSchema().dump(income)
        return None

    @staticmethod
    def update_income(income_id, data):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Update the income only if it belongs to the logged-in user
        income = Income.query.filter_by(id=income_id, user_id=user_id).first()
        if income:
            income.amount = data['amount']
            income.description = data['description']
            db.session.commit()
            return IncomeSchema().dump(income)
        return None

    @staticmethod
    def delete_income(income_id):
        # Decode the JWT token to get the user_id
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Delete the income only if it belongs to the logged-in user
        income = Income.query.filter_by(id=income_id, user_id=user_id).first()
        if income:
            db.session.delete(income)
            db.session.commit()
            return {'message': 'Income deleted successfully'}
        return {'message': 'Income not found'}
