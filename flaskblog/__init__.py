from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='e79e27c3bb345bd8965a34eda10a853e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#generate random key using secret module
# import secrets
# secrets.token_hex(16) => 16 = 16 bytes

db = SQLAlchemy(app)
from flaskblog import routes