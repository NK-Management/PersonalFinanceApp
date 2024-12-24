from flask import Blueprint, request, jsonify
from services.expense_tracking_service.app.services.income_service import IncomeService

bp = Blueprint('incomes', __name__)

@bp.route('/', methods=['POST'])
def create_income():
    data = request.get_json()
    result = IncomeService.create_income(data)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
def get_all_incomes():
    incomes = IncomeService.get_all_incomes()
    return jsonify([income.serialize() for income in incomes])
