from flask import Blueprint, request, jsonify
from services.expense_tracking_service.app.services.goal_service import GoalService

bp = Blueprint('goals', __name__)

@bp.route('/', methods=['POST'])
def create_goal():
    data = request.get_json()
    result = GoalService.create_goal(data)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
def get_all_goals():
    goals = GoalService.get_all_goals()
    return jsonify(goals)

@bp.route('/<int:id>', methods=['PUT'])
def update_goal(id):
    data = request.get_json()
    result = GoalService.update_goal(id, data)
    return jsonify(result)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_goal(id):
    result = GoalService.delete_goal(id)
    return jsonify(result)
