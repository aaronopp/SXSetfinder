from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
#from .server import block_until_token
#from utils import *

import urllib.request, urllib.parse, urllib.error, json
import csv
import pandas as pd

csv =  pd.read_csv('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/artists_3_13.csv') 
print(csv)
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"

user_artists = {0: 'Kendrick Lamar', 1: 'Kanye West', 2: 'John Mayer', 3: 'The Strokes', 4: 'Tame Impala', 5: 'The Undercover Dream Lovers', 6:'ZHU', 7:'Portugal. The Man', 
8:'Jay Chou', 9:'Taylor Swift', 10:'Spoon'
}
print(user_artists)
print(type(user_artists))

SXSW_artists = ['070 Shake', '16 the Olympus', '1982', '1kPhew', '1Playy' , "20 Somethin' Band/Tenth Child Inc. House Band", '24Hrs', '3 Hand Stephen', '5ive', '6Blocc', '90 One', 'A-RON', 'Aaron Lee Tasjan']

url = "http://smarterplaylists.playlistmachinery.com/frog/path";

start = time.time()

lowest_matches_dict = []
for key, user_artist in user_artists.items():
    print(user_artist)
    lowest_path_length = 15
    for artist in SXSW_artists:
        # print artist

        f = { 'src' : user_artist, 'dest' : artist}
        # f = { 'src' : 'Kendrick Lamar', 'dest' : '1982'}
        url_encoded = urllib.parse.urlencode(f)
        full_url = url + '?' + url_encoded
        # print full_url
        response = urllib.request.urlopen(full_url)
        data = json.loads(response.read())
        try:
            raw_path = data['raw_path']
        except KeyError as error:
            print('no match from boilthefrog')
        #print raw_path
        #print type(raw_path)
        path_length = len(raw_path)

        if path_length < lowest_path_length:
            # print 'lower than max'
            # print f
            lowest_match = f
            # print path_length
            lowest_path_length = path_length

    print('the lowest per your spotify top artist')
    print(lowest_path_length)
    print(lowest_match)
    lowest_matches_dict.append({"spotify_artist": lowest_match['src'], "SXSW_artist": lowest_match['dest'], "path_length": lowest_path_length})

    print(lowest_matches_dict)
#print data
print('took') 
print(time.time() - start)



def get_path_length(user_artist, sxsw_artist):
    f = { 'src' : user_artist, 'dest' : sxsw_artist}
    # f = { 'src' : 'Kendrick Lamar', 'dest' : '1982'}
    url_encoded = urllib.parse.urlencode(f)
    full_url = url + '?' + url_encoded
    # print full_url
    response = urllib.request.urlopen(full_url)
    data = json.loads(response.read())
    try:
        raw_path = data['raw_path']
    except KeyError as error:
        print('no match from boilthefrog')
    #print raw_path
    #print type(raw_path)
    path_length = len(raw_path)
    return path_length
