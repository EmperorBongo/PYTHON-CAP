from model import db, User, Question, Response, connect_to_db
from datetime import datetime

def create_user(email, username, password):
    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()

# create a question and add in the responses
def create_question(question_text, dateTime, a, b,c,d):
    
    new_question = Question(question_text=question_text, dateTime=dateTime,a=a,b=b,c=c,d=d,
                            a_count=0,b_count=0,c_count=0,d_count=0)
    db.session.add(new_question)
    db.session.commit()

    return new_question

# this is to get the questions that for the poll by date
def get_questions(date):
    return Question.query.filter_by(dateTime=date).first()


def create_response(user_id, question_id, response_text):

    new_response = Response(user_id=user_id, question_id=question_id, response_text=response_text )
    db.session.add(new_response)
    db.session.commit()
    return new_response


def get_responses_by_user(user_id):
    return Response.query.filter_by(user_id=user_id).first()

# this is to tally the responses
def tally_responses(poll_id):
    answers = Response.query.filter_by(question_id=poll_id).all()
    tally = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d": 0
    }
    for answer in answers:
        tally[answer.response_text] = tally.get(answer.response_text, 0) + 1
 
    question = Question.query.get(poll_id)
    question.a_count = tally['a']
    question.b_count = tally['b']
    question.c_count = tally['c']
    question.d_count = tally['d']
    db.session.commit()
    return tally


if __name__ == '__main__':
    from server import app
    connect_to_db(app)