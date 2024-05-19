from app import flaskApp, db
from flask_sqlalchemy import SQLAlchemy
from app import routes

import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User, Station, Post

# add a secure key in every form it generates (code from lecture)
flaskApp.config['SECRET_KEY'] = 'you-will-never-guess'
# add more variables here if needed

@flaskApp.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    flaskApp.run(debug=True)
