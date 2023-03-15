import os

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY') 
    SECRET_KEY = 'd1977121aa0c44c245afcb47d5268264'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@localhost:5432/trivia_questions'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
