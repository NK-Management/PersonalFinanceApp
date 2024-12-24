from services.expense_tracking_service.app.utils.db import db, Base

class Jar(Base):
    __tablename__ = 'jars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('public.users.id'), nullable=False)  # Link to logged-in user

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'balance': self.balance,
            'user_id': self.user_id  # Include user information in serialization
        }
