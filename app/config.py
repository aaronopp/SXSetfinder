import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'youll-never-get-this'
	WTF_CSRF_SECRET_KEY="a csrf secret key"