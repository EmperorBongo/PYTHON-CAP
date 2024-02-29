from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash
from model import User
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined
app.app_context().push()

@app.route('/')
def base():
    return render_template('dashboard.html')

@app.route('/home')
def home():
    return render_template('home.html')

#Home page has includes profile of user statistics and a button to go to polls

@app.route("/create_user", methods=['POST'])
def create_user():
    """View all users."""
    email = request.form.get('email')
    password = request.form.get('password')
    

    
    users = crud.create_user(email, "usernameexample", password, 1, "asdf", "asdf", "asdf")
    print(users)

    return render_template("all_users.html", users=users)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # User is authenticated, store user ID in session
        session['user_id'] = user.user_id
        return redirect(url_for('home'))
    else:
        return render_template('dashboard.html', error='Invalid username or password')


@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)




