# from flask import Flask, jsonify, render_template, url_for, request
from flask import Flask
# from flask_cors import CORS
# from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_caching import Cache



app = Flask(__name__)
app.config['SECRET_KEY'] = '0a8e6b76febb87fbb68815bcaa7f1584'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['CACHE_TYPE'] = "RedisCache"
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
cache = Cache(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from backend import routes
