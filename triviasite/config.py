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
