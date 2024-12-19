from authentication_service.app.models.user import User, db


class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """Retrieve a user by their ID."""
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    @staticmethod
    def get_user_by_email(email):
        """Retrieve a user by their email."""
        user = User.query.filter_by(email=email).first()
        if not user:
            raise ValueError(f"User with email {email} not found.")
        return user

    @staticmethod
    def create_user(data):
        """
        Create a new user.
        
        :param data: A dictionary with keys 'username', 'email', 'password', and optionally 'role'.
        """
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role", "user")  # Default role is 'user'

        # Check if the username or email already exists
        if User.query.filter((User.username == username) | (User.email == email)).first():
            raise ValueError("A user with this username or email already exists.")

        # Create a new user
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user_role(user_id, new_role):
        """
        Update the role of a user.
        
        :param user_id: The ID of the user whose role is to be updated.
        :param new_role: The new role to assign to the user.
        """
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        
        user.role = new_role
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        """Retrieve a list of all users."""
        return User.query.all()
