from flask import request
from services.expense_tracking_service.app import db
from services.expense_tracking_service.app.models.expense import Expense
from services.expense_tracking_service.app.schemas.expense_schema import ExpenseSchema
from services.expense_tracking_service.app.utils.jwt_handler import decode_jwt

class ExpenseService:
    @staticmethod
    def create_expense(data):
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        expense = Expense(
            amount=data['amount'], 
            description=data['description'], 
            jar_id=data['jar_id'], 
            user_id=user_id  # Associate expense with the logged-in user
        )
        db.session.add(expense)
        db.session.commit()
        return ExpenseSchema().dump(expense)

    @staticmethod
    def get_all_expenses():
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch only the logged-in user's expenses
        expenses = Expense.query.filter_by(user_id=user_id).all()
        return ExpenseSchema(many=True).dump(expenses)

    @staticmethod
    def get_expense_by_id(expense_id):
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch the expense only if it belongs to the logged-in user
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()
        if expense:
            return ExpenseSchema().dump(expense)
        return None

    @staticmethod
    def update_expense(expense_id, data):
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Update the expense only if it belongs to the logged-in user
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()
        if expense:
            expense.amount = data['amount']
            expense.description = data['description']
            expense.jar_id = data['jar_id']
            db.session.commit()
            return ExpenseSchema().dump(expense)
        return None

    @staticmethod
    def delete_expense(expense_id):
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Delete the expense only if it belongs to the logged-in user
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()
        if expense:
            db.session.delete(expense)
            db.session.commit()
            return {'message': 'Expense deleted successfully'}
        return {'message': 'Expense not found'}
