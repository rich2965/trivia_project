from datetime import datetime
from itsdangerous import URLSafeTimedSerializer  as Serializer
from triviasite import db
from flask import current_app

class Question(db.Model):
    __tablename__ = 'question_random'
    id = db.Column(db.Text,primary_key=True)
    question = db.Column(db.Text,nullable=False)
    answer = db.Column(db.Text,nullable=False)
    source = db.Column(db.Text,nullable=False)
    category = db.Column(db.Text,nullable=False)

class Movie(db.Model):
    __tablename__ = 'movie_us_popular_vw'
    id = db.Column(db.Text,primary_key=True)
    titleType = db.Column(db.Text,nullable=False)
    primaryTitle = db.Column(db.Text,nullable=False)
    startYear = db.Column(db.Text,nullable=False)
    genres = db.Column(db.Text,nullable=False)
    still_image = db.Column(db.Text,nullable=False)
    still_imagery = db.Column(db.Text,nullable=False)
    storyline = db.Column(db.Text,nullable=False)
