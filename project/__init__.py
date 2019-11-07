from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)

from project.models import User