from flask import Blueprint, request, jsonify
from services.expense_tracking_service.app.services.expense_service import ExpenseService

bp = Blueprint('expenses', __name__)

@bp.route('/', methods=['POST'])
def create_expense():
    data = request.get_json()
    result = ExpenseService.create_expense(data)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
def get_all_expenses():
    expenses = ExpenseService.get_all_expenses()
    return jsonify(expenses)

@bp.route('/<int:id>', methods=['PUT'])
def update_expense(id):
    data = request.get_json()
    result = ExpenseService.update_expense(id, data)
    return jsonify(result)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_expense(id):
    result = ExpenseService.delete_expense(id)
    return jsonify(result)
