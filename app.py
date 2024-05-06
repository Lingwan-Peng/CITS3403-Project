from app import flaskApp
from flask_sqlalchemy import SQLAlchemy
from app import routes

# add a secure key in every form it generates (code from lecture)
# flaskApp.config['SECRET_KEY'] = 'you-will-never-guess'
# add more variables here if needed


if __name__ == "__main__":
    flaskApp.run(debug=True)
