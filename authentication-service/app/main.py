from app import create_app, db
from app.models.user import User

app = create_app()

@app.before_first_request
def create_tables_and_admin():
    db.create_all()
    if not User.query.filter_by(email="admin@example.com").first():
        admin = User(username="admin", email="admin@example.com", role="admin")
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
