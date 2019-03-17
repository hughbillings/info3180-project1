from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should mae this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning
UPLOAD_FOLDER='./app/static/uploads'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
