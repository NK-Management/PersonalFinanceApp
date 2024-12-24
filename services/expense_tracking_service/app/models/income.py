from services.expense_tracking_service.app.utils.db import db, Base
from sqlalchemy.orm import relationship

class Income(Base):
    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('public.users.id'), nullable=False)  # Link to logged-in user

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'user_id': self.user_id  # Include user information in serialization
        }
