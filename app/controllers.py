from app.models import User, Station, Post
from app import db, flaskApp, render_template

@flaskApp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@flaskApp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

class GroupCreationError(Exception):
    pass

# if user is None: