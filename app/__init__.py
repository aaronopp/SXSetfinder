from flask import Flask
from config import Config#, basedir
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config.update(dict(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'youll-never-get-this',
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
# app.debug = True
# app.run(host = '0.0.0.0',port=5005)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models