from services.expense_tracking_service.app import ma
from services.expense_tracking_service.app.models.expense import Expense

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        load_instance = True
