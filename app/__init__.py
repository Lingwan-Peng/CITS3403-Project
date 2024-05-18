from flask import Flask, render_template, url_for
from flask_login import LoginManager



flaskApp = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(flaskApp)
login_manager.login_view = 'login_func' 
from config import Config 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)

from app import routes, models # don't move this line
