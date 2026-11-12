from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///db.sqlite3'
)
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'dev'
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models, views, error_handlers, cli_commands