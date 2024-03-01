from flask import Flask, render_template, jsonify, request
import processor
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for



app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/user_profile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/register', methods=["GET","POST"])
def register():
     if request.method == 'POST':
         response = reg(request.form['name'],request.form['email'],request.form['password'])
         return jsonify({"response": response })
     elif request.method == 'GET':
         return render_template('register.html', **locals())





@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })

def reg(name, email, password):
    try:
        # Create a new user instance
        new_user = User(name=name, email=email, password=password)

        # Add the user to the database session
        db.session.add(new_user)

        # Commit the changes to the database
        db.session.commit()

        # Success message
        return "user created"

    except Exception as e:
        # Handle any potential errors during database operations
        db.session.rollback()  # Rollback changes in case of errors
        return "user not created"


if __name__ == '__main__':
    app.run(port=5500)



