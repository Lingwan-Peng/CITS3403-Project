from flask import Flask, render_template, url_for

flaskApp = Flask(__name__)

from app import routes