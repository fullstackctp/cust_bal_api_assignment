from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY'] = '98bbfaf96b620646fb6a3eefb3e4302d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)

from api import routes

