from datetime import datetime
from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	city = db.Column(db.String(64), index=True)
	password_hash = db.Column(db.String(128))
	artists = db.relationship('TopArtists', backref='author', lazy='dynamic')
	def __repr__(self):
		return '<User {}>'.format(self.username)

class TopArtists(db.Model):
	spotify_username = db.Column(db.String(64), primary_key=True)
	username = db.Column(db.String(64), db.ForeignKey('user.username'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	top_artists = db.Column(db.Text(1000), index=True)

	def __repr__(self):
		return '<TopArtists {}>'.format(self.top_artists)


