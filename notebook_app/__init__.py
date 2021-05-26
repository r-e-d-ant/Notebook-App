
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwqedfdfgwergrwgewrggewgwegwegwegew'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notebooks.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "signin"
login_manager.login_message_category = "info"

from notebook_app import routes