from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

# Setting basedir for db
basedir = os.path.abspath(os.path.dirname(__file__))

# creating app
app = Flask(__name__)

# app cfg
app.config["SECRET_KEY"] = "mOT8N26ZqWw2OZl18OZD4zFcuFokVyla"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# creating db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# creating login manager
login = LoginManager(app)
login.login_view = 'login'


from app import views, models

