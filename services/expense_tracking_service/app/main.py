from services.expense_tracking_service.app import create_app, db
from services.expense_tracking_service.app.models.jar import Jar
from services.expense_tracking_service.app.models.expense import Expense
from services.expense_tracking_service.app.models.goal import Goal
from services.expense_tracking_service.app.models.income import Income
from services.expense_tracking_service.app.utils.db import reflect_users_table
from sqlalchemy import Table


app = create_app()

def init_db():
    with app.app_context():
        try:
            reflect_users_table(app)
            db.create_all()
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error initializing database: {e}")


if __name__ == "__main__":
    # Initialize the database
    print("Initializing database...")
    init_db()

    print("Starting the application...")
    # Run the Flask application
    app.run(debug=True)
