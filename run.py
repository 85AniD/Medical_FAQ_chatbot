from app import app, db
from admin import admin_blueprint

app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
