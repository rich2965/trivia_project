import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer  as Serializer
from triviasite import db, login_manager
from flask_login import UserMixin
from flask import current_app

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'postgresql://root:root@localhost:5432/trivia_questions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Question(db.Model):
    id = db.Column(db.Text,primary_key=True)
    question = db.Column(db.Text,nullable=False)
    answer = db.Column(db.Text,nullable=False)
    source = db.Column(db.Text,nullable=False)
    category = db.Column(db.Text,nullable=False)

