import os

class Config:
        SQLALCHEMY_DATABASE_URI = 'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
                db_user=os.environ.get('db_user'),
                db_password=os.environ.get('db_password'),
                db_name=os.environ.get('db_name'),
                db_host=os.environ.get('db_host'),
                db_port=os.environ.get('db_port')
        )

