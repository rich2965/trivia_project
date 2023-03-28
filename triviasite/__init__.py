from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from triviasite.config import Config


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from triviasite.main.routes import main
from triviasite.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(errors)

if __name__ == '__main__':
    app.run()