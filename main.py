from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
import os
from sqlalchemy_utils import create_database, database_exists
app = Flask(__name__)
app.secret_key = os.urandom(24)
botname = "AniD"



url = "mysql://root:@localhost/user_profile"
if not database_exists(url):
    create_database(url)

# Configure SQLAlchemy database connection (avoid direct database connection)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/user_profile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    # Constructor for model initialization (optional)
   

# Function to create the database (recommended approach)
def create_user_profile_database():
    """Creates the 'user_profile' database if it doesn't already exist."""

    with app.app_context():  # Ensure application context
        db.create_all()  # Create all database tables defined in the models

# Execute the database creation function
create_user_profile_database()




