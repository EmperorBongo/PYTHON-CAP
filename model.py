from flask_sqlalchemy import SQLAlchemy 
import json

db = SQLAlchemy()



class User(db.Model): 
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User user_id={self.user_id}, username={self.username}>"

    # Define relationship to questions


class Question(db.Model):
    __tablename__ = "questions"

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.Text, nullable=False)
    dateTime = db.Column(db.DateTime, default=False)
    a = db.Column(db.Text)
    b = db.Column(db.Text)
    c = db.Column(db.Text)
    d = db.Column(db.Text)
    a_count = db.Column(db.Integer)
    b_count = db.Column(db.Integer)
    c_count = db.Column(db.Integer)
    d_count = db.Column(db.Integer)

    responses = db.relationship('Response', backref='question', lazy=True)

    def __repr__(self):
        return f"<Question question_id={self.question_id}, question_text={self.question_text}>"

class Response(db.Model):
    __tablename__ = "responses"

    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    response_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Response response_id={self.response_id}, user_id={self.user_id}, question_id={self.question_id}>"
    

def connect_to_db(flask_app, db_uri="postgresql://bbrbr:9822@localhost:5432/polls", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    with app.app_context(): 
        connect_to_db(app)