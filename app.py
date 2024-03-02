from flask import Flask, render_template, jsonify, request
import processor
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
from flask_session import Session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/user_profile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


def loggedin(func):
    def secure_function():
        if  not session.get("email") or  not session.get("password"):
            return redirect("/login")
        else:
            if lgin(session.get("email"), session.get("password")):
                return func()
            else:
                return redirect("/login")

    return secure_function

def loggedout(func):
    def secure_function():  # Corrected misspelling
        if "email" not in session or "password" not in session:
            return func()
        else:
            if lgin(session.get("email"), session.get("password")):
                return redirect("/")
            else:
                return func()

    return secure_function


@app.route('/', methods=["GET", "POST"])
@loggedin
def index():
    return render_template('index.html', **locals())

@app.route('/register', methods=["GET","POST"])
def register():
     if request.method == 'POST':
         response = reg(request.form['name'],request.form['email'],request.form['password'])
         return jsonify({"response": response })
     elif request.method == 'GET':
         return render_template('register.html', **locals())





@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if lgin(request.form['email'],request.form['password']):
            session["email"]=request.form['email']
            session["password"]=request.form['password']
            return jsonify({"response": "login successful" ,"status":"true"})
        else:
            return jsonify({"response": "login failed" ,"status":"false" })
    elif request.method == 'GET':
        return render_template('login.html', **locals())
   
    

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })

def reg(name, email, password):
    user = User.query.filter_by(email=email).first()

        # Return True if a user with the email is found, False otherwise
        
    if user is not None:
        return "email already exsists"
    
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


def lgin(email,password):
    try:
        # Query the database for a user with the given email
        user = User.query.filter_by(email=email).first()

        # Check if user exists and password matches (if user is found)
        if user and user.password == password:
            return True
        else:
            return False

    except Exception as e:
        # Handle potential errors during database operations
  
        return False





if __name__ == '__main__':
    app.run(port=5500)



