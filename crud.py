from model import db, User, Question, Response, connect_to_db

def create_user(email, username, password, age, gender, occupation, state):
    new_user = User(email=email, username=username, password=password, age=age, gender=gender, occupation=occupation, state=state)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()

def update_user(user_id, email=None, username=None, password=None, age=None, gender=None, occupation=None, state=None):
    user = User.query.get(user_id)
    if user:
        if email:
            user.email = email
        if username:
            user.username = username
        if password:
            user.password = password
        if age:
            user.age = age
        if gender:
            user.gender = gender
        if occupation:
            user.occupation = occupation
        if state:
            user.state = state
        db.session.commit()
        return user
    
def create_question(question_text, dateTime=None):
    
    new_question = Question(question_text=question_text, dateTime=dateTime)
    db.session.add(new_question)
    db.session.commit()
    return new_question

def get_questions():
    return Question.query.all()

def create_response(user_id, question_id, response_text):

    new_response = Response(user_id=user_id, question_id=question_id, response_text=response_text )
    db.session.add(new_response)
    db.session.commit()
    return new_response


def get_responses_by_user(user_id):
    return Response.query.filter_by(user_id=user_id)

# def get_responses_by_question(question_id):
#     return Response.query.filter_by

 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


# TODO error handling