from datetime import datetime
from triviasite import db


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
    characters = db.Column(db.Text,nullable=False)
    directorName = db.Column(db.Text,nullable=False)

class People(db.Model):
    __tablename__ = 'people_popular_vw'
    person_id = db.Column(db.Text,primary_key=True)
    primaryName = db.Column(db.Text,nullable=False)
    birthYear = db.Column(db.Text,nullable=False)
    deathYear = db.Column(db.Text,nullable=False)
    primaryProfession = db.Column(db.Text,nullable=False)
    knownForList = db.Column(db.Text,nullable=False)
    imagery = db.Column(db.Text,nullable=False)

class Event(db.Model):
    __tablename__ = 'events_vw'
    id =  db.Column(db.Integer,primary_key=True)
    event_year = db.Column(db.Text,primary_key=True)
    event_date = db.Column(db.Text,nullable=False)
    event_type = db.Column(db.Text,nullable=False)
    event_desc = db.Column(db.Text,nullable=False)

class Country(db.Model):
    __tablename__ = 'countries_vw'
    name = db.Column(db.Text,primary_key=True)
    continent = db.Column(db.Text,nullable=False)
    latitude = db.Column(db.Text,nullable=False)
    longitude = db.Column(db.Text,nullable=False)
    capital_city = db.Column(db.Text,nullable=False)
    population = db.Column(db.Text,nullable=False)
    languages = db.Column(db.Text,nullable=False)
    currency = db.Column(db.Text,nullable=False)
    points_of_interest = db.Column(db.Text,nullable=False)
    geography_nature = db.Column(db.Text,nullable=False)
    neighbor_countries = db.Column(db.Text,nullable=False)