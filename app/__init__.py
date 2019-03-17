from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should mae this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lobvwtloxzfgak:ea9bcec6f62112652616cbc60bc8cdd543d57a07a1cc71b07436bca22ab72388@ec2-54-221-236-144.compute-1.amazonaws.com:5432/d5768p723rjbsq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning
UPLOAD_FOLDER='./app/static/uploads'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
