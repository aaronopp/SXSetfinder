from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
from .server import block_until_token
from .utils import *

@app.route('/')

@app.route('/index')
def index():
    user = {'username' : 'User'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('went thru')
        flash('Login requested for user {}, remember_me={}'.format(
            form.firstname.data, form.remember_me.data))
        return redirect(url_for('index'))
    else: 
        print('didnt go thru')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/spotify', methods=['GET', 'POST'])
def spotify():
    form = SpotifyForm()
    scope = 'user-top-read user-read-playback-state user-read-recently-played'
    print('at spotify')
    if form.validate_on_submit():
        print('spotify form went thru')

        #scope = 'user-read-playback-state user-read-recently-played'
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect',  scope=scope)
        auth_url = sp_oauth.get_authorize_url()
        
        webbrowser.open(auth_url)
        token = block_until_token(sp_oauth)

        #token = util.prompt_for_user_token('aaronopp', scope, client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect')
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace=False
            #ranges = ['short_term', 'medium_term', 'long_term']
            #print 'token went thru!'
            #for range in ranges:
                #print "range:", range
            artist_results = sp.current_user_top_artists(time_range='short_term', limit=50)
            for i, item in enumerate(artist_results['items']):
                print(i, item['name'])
            save_obj(artist_results, 'top_artists')

            song_results = sp.current_user_top_tracks(time_range='short_term', limit=50)
            print(type(artist_results))
            for i, item in enumerate(song_results['items']):
                print(i, item['name'])
            print()
        else:
            print('cant get token for', form.spotify_username.data)

    #else:
        #print 'spotify form didnt go thru'
    return render_template('spotify.html', form=form)
    #token = util.prompt_for_user_token('aaronopp', scope, client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect')
# @app.route('/boil', methods['GET', 'POST'])
# def boil():
    
