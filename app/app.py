import re
from flask import Flask
from . import nav_bar, simple_pages
from app.extenstions.login_manager import login_manager
from app.extenstions.database import db, migrate
from app.nav_bar.models import User
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config['SECRET_KEY'] = "Thisisupposedtobeasecretkey"
    
  
    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
  app.register_blueprint(nav_bar.routes.blueprint)
  app.register_blueprint(simple_pages.routes.simple_pages)



def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)



# def initialize_login_manager(app: Flask):
#   login_manager = LoginManager(app)
#   return login_manager

# app = create_app()
# login_manager = LoginManager()
# login_manager.init_app(app)
