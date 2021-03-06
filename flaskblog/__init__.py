from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_fontawesome import FontAwesome

app = Flask(__name__)
app.config['SECRET_KEY']='e79e27c3bb345bd8965a34eda10a853e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
fa = FontAwesome(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from flaskblog import routes