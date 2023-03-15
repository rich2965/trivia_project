from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from triviasite.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view ='login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from triviasite.users.routes import users
    from triviasite.questions.routes import questions
    from triviasite.main.routes import main
    from triviasite.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(questions)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app