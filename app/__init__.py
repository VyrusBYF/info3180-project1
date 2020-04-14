from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://madploopgrgiol:e02d1aec3f58afe489f1f48a951866199ff69f61cd79c70d33b77a8056d21d44@ec2-34-204-22-76.compute-1.amazonaws.com:5432/d139behheo8d0r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
UPLOAD_FOLDER =  './app/static/uploads'

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
