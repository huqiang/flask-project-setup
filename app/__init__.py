from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager
)
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
print(app.url_map)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' +os.path.join(basedir, 'db/db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret'
jwt=JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from app.models import *
from app.routes import *