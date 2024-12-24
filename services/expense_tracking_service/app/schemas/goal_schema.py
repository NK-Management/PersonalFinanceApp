from services.expense_tracking_service.app import ma
from services.expense_tracking_service.app.models.goal import Goal

class GoalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Goal
        load_instance = True
