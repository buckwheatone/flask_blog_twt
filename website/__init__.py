from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail 
from website.config import Config
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = "helloworld"
    
    
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from website.views import views
    from website.auth import auth
    from website.errors.handlers import errors

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(errors, url_prefix="/")

    create_database(app)

    return app


def create_database(app):
    if not path.exists("website/" + Config.DB_NAME):
        db.create_all(app=app)
