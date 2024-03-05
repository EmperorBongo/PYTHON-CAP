from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from model import User
import crud
from jinja2 import StrictUndefined
import os
import pusher


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined
app.app_context().push()
pusher_client = pusher.Pusher(
  app_id='1766272',
  key='d38373f08e722507620c',
  secret='c8aebb7b27c27f42c92a',
  cluster='mt1',
  ssl=True
)
pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})




@app.route('/')
def base():
    return render_template('dashboard.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/polls')
def polls():

    polls = crud.get_questions()

    return render_template('polls.html', polls=polls)

@app.route("/create_user", methods=['POST'])
def create_user():
    """View all users."""
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    gender = request.form.get('gender')
    occupation = request.form.get('occupation')
    state = request.form.get('state')
    

    
    users = crud.create_user(email, username, password, age, gender, occupation, state)
    print(users)

    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)
    users = User.query.filter_by(email=email).first()
    print(users, users.password)
    if users and users.password == password:
        
        session['user_id'] = users.user_id

        print("Session Data:", session)

        return redirect('/home')
    else:
        return render_template('dashboard.html', error='Invalid username or password')
    

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('login'))

@app.route('/update_user', methods=['GET'])
def update_user():
    user_id = request.form.get('user_id')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    gender = request.form.get('gender')
    occupation = request.form.get('occupation')
    state = request.form.get('state')


    updated_user = crud.update_user(user_id, email, username, password, age, gender, occupation, state)

    if updated_user:
        return redirect('/home')
    else:
        return "User not found", 404

if __name__ == '__main__':
    from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True)




