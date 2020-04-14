from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qudzbqqlashgur:98a208eb1f38cd7edd45326b23f65d66e6389e0487608203d52330cb5efde536@ec2-34-197-212-240.compute-1.amazonaws.com:5432/d5enson5ggltov'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
UPLOAD_FOLDER =  './app/static/uploads'

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
