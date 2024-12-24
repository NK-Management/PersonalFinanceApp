from services.expense_tracking_service.app.utils.db import db, Base
from sqlalchemy.orm import relationship

class Goal(Base):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('public.users.id'), nullable=False)  # Link to logged-in user

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'target_amount': self.target_amount,
            'current_amount': self.current_amount,
            'user_id': self.user_id  # Include user information in serialization
        }
