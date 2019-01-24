## App Utilities
import os
import env
from db import db

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['DEBUG'] = True

Bootstrap(app)

from project.users.views import users_blueprint
from project.library.views import library_blueprint
from project.algorithms.views import algorithms_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(library_blueprint)
app.register_blueprint(algorithms_blueprint)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host = '0.0.0.0')
