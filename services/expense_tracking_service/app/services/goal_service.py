from flask import request
from services.expense_tracking_service.app import db
from services.expense_tracking_service.app.models.goal import Goal
from services.expense_tracking_service.app.schemas.goal_schema import GoalSchema
from services.expense_tracking_service.app.utils.jwt_handler import decode_jwt

class GoalService:
    @staticmethod
    def create_goal(data):
        # Decode JWT to get the user_id of the logged-in user
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Create a new goal and associate it with the logged-in user
        goal = Goal(
            name=data['name'],
            target_amount=data['target_amount'],
            current_balance=data['current_balance'],
            user_id=user_id  # Associate goal with the logged-in user
        )
        db.session.add(goal)
        db.session.commit()
        return GoalSchema().dump(goal)

    @staticmethod
    def get_all_goals():
        # Decode JWT to get the user_id of the logged-in user
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch only the logged-in user's goals
        goals = Goal.query.filter_by(user_id=user_id).all()
        return GoalSchema(many=True).dump(goals)

    @staticmethod
    def get_goal_by_id(goal_id):
        # Decode JWT to get the user_id of the logged-in user
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Fetch the goal only if it belongs to the logged-in user
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if goal:
            return GoalSchema().dump(goal)
        return None

    @staticmethod
    def update_goal(goal_id, data):
        # Decode JWT to get the user_id of the logged-in user
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Update the goal only if it belongs to the logged-in user
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if goal:
            goal.name = data['name']
            goal.target_amount = data['target_amount']
            goal.current_balance = data['current_balance']
            db.session.commit()
            return GoalSchema().dump(goal)
        return None

    @staticmethod
    def delete_goal(goal_id):
        # Decode JWT to get the user_id of the logged-in user
        user_id = decode_jwt(request.headers.get('Authorization'))['user_id']
        # Delete the goal only if it belongs to the logged-in user
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
        if goal:
            db.session.delete(goal)
            db.session.commit()
            return {'message': 'Goal deleted successfully'}
        return {'message': 'Goal not found'}
