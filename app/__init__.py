from flask import Flask, render_template, url_for

flaskApp = Flask(__name__)

from config import Config 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)

from app import routes, models # don't move this line
