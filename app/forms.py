from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	firstname = StringField('First name:', validators=[DataRequired()])
	lastname = StringField('Last name:', validators=[DataRequired()])
	email = StringField('Email:', validators=[DataRequired()])
	city = StringField('City:', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class SpotifyForm(FlaskForm):
	spotify_username = StringField('Spotify Username:', validators=[DataRequired()])
	submit = SubmitField('Login')

	
	