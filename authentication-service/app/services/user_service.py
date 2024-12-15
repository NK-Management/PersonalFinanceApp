from app.models.user import User, db

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(username, email, password, role="user"):
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user_role(user_id, new_role):
        user = User.query.get(user_id)
        if user:
            user.role = new_role
            db.session.commit()
        return user
