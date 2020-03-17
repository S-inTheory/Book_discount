import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False
