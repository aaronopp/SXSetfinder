from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
from .server import block_until_token

# scope = 'user-top-read user-read-playback-state user-read-recently-played'
# print 'at spotify'


#scope = 'user-read-playback-state user-read-recently-played'
# sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id='dbe2a20785304190b8e35d5d6644397b', 
# 	client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect',  scope=scope)
# print 'sp oauth', sp_oauth
# auth_url = sp_oauth.get_authorize_url()


auth_url = 'https://oauth.groupme.com/oauth/login_dialog?client_id=QiZzLzcPd3XNLTsLZJrLfdOJmYBW9tGJq0uLETug'
webbrowser.open(auth_url)