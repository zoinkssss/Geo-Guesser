from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import environ

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("Config." + environ.get('FLASK_ENV').capitalize())

    with app.app_context():

        db.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)

        from .Home import Home
        from .Authenticator import Auth

        app.register_blueprint(Home.home_bp)
        app.register_blueprint(Auth.auth_bp)

    return app 
        

       




        
   