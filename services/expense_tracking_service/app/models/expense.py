from services.expense_tracking_service.app.utils.db import db, Base
from sqlalchemy.orm import relationship

class Expense(Base):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    jar_id = db.Column(db.Integer, db.ForeignKey('jars.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('public.users.id'), nullable=False)  # Link to logged-in user
    jar = relationship('Jar', backref='expenses')

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'jar_id': self.jar_id,
            'user_id': self.user_id  # Include user information in serialization
        }
