import os

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY') 
    SECRET_KEY = 'd1977121aa0c44c245afcb47d5268264'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
            db_user=os.environ.get('db_user'),
            db_password=os.environ.get('db_password'),
            db_name=os.environ.get('db_name'),
            db_host=os.environ.get('db_host'),
            db_port=os.environ.get('db_port')
    )
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
