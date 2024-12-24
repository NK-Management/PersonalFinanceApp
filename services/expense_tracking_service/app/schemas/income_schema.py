from services.expense_tracking_service.app import ma
from services.expense_tracking_service.app.models.income import Income

class IncomeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Income
        load_instance = True
