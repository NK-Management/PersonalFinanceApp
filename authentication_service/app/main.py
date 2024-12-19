from authentication_service.app import create_app, db
from authentication_service.app.models.user import User
from sqlalchemy import inspect

app = create_app()


# Use a flag to ensure the logic only runs once
has_initialized = False

@app.before_request
def create_tables_and_admin():
    global has_initialized
    if not has_initialized:
        print("This runs only before the first request!")
        
        # Check if tables exist using SQLAlchemy's inspector
        inspector = inspect(db.engine)
        if not inspector.get_table_names():
            db.create_all()
            print("Database tables created successfully.")
        else:
            print("Database tables already exist.")

        # Optional: Add admin user if not already created
        # if not User.query.filter_by(email="nachikunik29@gmail.com").first():
        #     admin = User(username="nachiketa_balar", email="nachikunik29@gmail.com", role="admin")
        #     admin.set_password("P@ssw0rd@123")
        #     db.session.add(admin)
        #     db.session.commit()
        #     print("Admin user created successfully."
        
        has_initialized = True


if __name__ == "__main__":
    app.run(debug=True)