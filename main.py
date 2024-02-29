from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
import os
import mysql.connector as sqltr
import text_process

app = Flask(__name__)
app.secret_key = os.urandom(24)
botname = "AniD"

# Define the SQLAlchemy instance
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://newuser:password@localhost/user_profile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Database connection setup
conn = sqltr.connect(host="localhost", user="root", password="", database="user_profile")
cur = conn.cursor()
