from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from model import User
import crud
from jinja2 import StrictUndefined
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SECRET_KEY"
app.jinja_env.undefined = StrictUndefined
app.app_context().push()

@app.route('/')
def base():
    
    return render_template('login.html')

@app.route('/home')
def home():
    
    return render_template('home.html')

@app.route('/polls')
def polls():

    poll = crud.get_questions(datetime.today().date())

    return render_template('polls.html', poll=poll)

@app.route('/create_quest')
def create_quest():
    return render_template('create_question.html')

@app.route('/create_question', methods=['POST'])
def create_question():

    # crud.create_question('What dog is best?', datetime.today().date(), 'Great Dane', 'Poodle', 'Pointer', 'Yorkie')
   
    question_text = request.form.get('question_text')
    dateTime = request.form.get('date')
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')
    d = request.form.get('d')

    new_date = datetime.strptime(dateTime, "%Y-%d-%m")
    new_question = crud.create_question(question_text, new_date, a, b, c, d)
    print(new_question)
    return redirect('/home')

@app.route("/log-response", methods=['POST'])
def log_response():
    response = request.json.get('response')

    poll = crud.get_questions(datetime.today().date())
    crud.create_response(session['user_id'],poll.question_id, response)
    tally = crud.tally_responses(poll.question_id)
    total_count = 0

    for num in tally.values():
        total_count += num
    tally['total'] = total_count
    
    return jsonify(tally)

@app.route('/create_account')
def create_account():

    return render_template('create_account.html')

@app.route("/create_user", methods=['POST'])
def create_user():
    """View all users."""
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    
    user = crud.create_user(email, username, password)
    session['user_id'] = user.user_id
    print(user)

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
        return render_template('login.html', error='Invalid username or password')
    
@app.errorhandler(404)
def error_404(e): 
   return render_template("404.html") 

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return render_template('login.html')

if __name__ == '__main__':
    from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True)


