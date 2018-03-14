from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time
from config  import Config
import webbrowser
from .server import block_until_token
from .utils import *
import urllib


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
        #sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect',  scope=scope)
        #auth_url = sp_oauth.get_authorize_url()
        
        #webbrowser.open(auth_url)
        #token = block_until_token(sp_oauth)
        #print('data', form.spotify_username.data)
        token = util.prompt_for_user_token('kushaan', scope, client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:3000')
        if token:
            top_artists = []
            sp = spotipy.Spotify(auth=token)
            #print(sp.user())
            username = sp.user('kushaan')
            
            sp.trace=False
            #ranges = ['short_term', 'medium_term', 'long_term']
            #print 'token went thru!'
            #for range in ranges:
                #print "range:", range
            artist_results = sp.current_user_top_artists(time_range='short_term', limit=50)
            for i, item in enumerate(artist_results['items']):
                print(i, item['name'])
                top_artists.append(item['name'])

                if i > 10:
                    break
            
            user_artists = []
            for top in top_artists:
                user_artists.append(top.encode('ascii','ignore')) 
            with open('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/app/artist_list_trimmed_final.csv', 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
                artist_list_3_15_f = your_list[0]


            lowest_matches_dict = get_lowest_artist_matches(user_artists[:3], artist_list_3_15_f)

            predicted_artists = []
            for value in lowest_matches_dict:
                predicted_artists.append(value['SXSW_artist'])
    
            predicted_artists = set(list(predicted_artists))
            print('DONE', predicted_artists)
            # song_results = sp.current_user_top_tracks(time_range='short_term', limit=50)
            # print(type(artist_results))
            # for i, item in enumerate(song_results['items']):
            #     print(i, item['name'])
            # print()
        else:
            print('cant get token for', form.spotify_username.data)

    #else:
        #print 'spotify form didnt go thru'
    return render_template('spotify.html', form=form)

@app.route('/groupme', methods=['GET', 'POST'])
def groupme():
    from groupy.client import Client
    import datetime

    def makeGroup(n, usrList):
        client = Client.from_token('jI9arGAkDrtNWAhKdKLnjaj182R2L7RLV7q9odFj')
        now=datetime.datetime.now()
        nDate = n+now.strftime()
        new_group = client.groups.create(name=nDate)
        for i in usrList:
            new_group.memberships.add(i[0], None, i[1], None)

    testList=[['aaron', '8583533185'], ['ranga', '7329978242']]
    makeGroup('test', testList)
    #token = util.prompt_for_user_token('aaronopp', scope, client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect')
# @app.route('/boil', methods['GET', 'POST'])
# def boil():
    
