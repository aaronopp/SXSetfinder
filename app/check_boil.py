from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
from .server import block_until_token
from .utils import *

import urllib.request, urllib.parse, urllib.error, json
import csv
import pandas as pd

url = "http://smarterplaylists.playlistmachinery.com/frog/path";

raw_csv =  pd.read_csv('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/app/artist_list_trimmed_final.csv') 
# raw_csv =  pd.read_csv('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/app/events.csv') 
raw_csv.columns = ['artist']
print(raw_csv)
# artist_list =  raw_csv['artistname'].tolist()
artist_list = raw_csv['artist'].tolist()
artist_list_trimmed = []
# with open('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/artists_3_13.csv', 'rb') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
# print 'my list', your_list
# print artist_list_old
#artist_list_old = raw_csv.values.T
# for art in artist_list_old:
# 	print art
# print type(artist_list_old)
# artist_list  = [l[0] for l in artist_list_old]
# print artist_list
#for value in csv:
#for key, value in csv:
	#print value
# artist_list_trimmed = []

for artist in artist_list[:15]:
        # print artist
        print(artist)

        f = { 'src' : 'Kendrick Lamar', 'dest' : artist}
        # f = { 'src' : 'Kendrick Lamar', 'dest' : '1982'}
        url_encoded = urllib.parse.urlencode(f)
        full_url = url + '?' + url_encoded
        # print full_url
        response = urllib.request.urlopen(full_url)
        data = json.loads(response.read())
        try:
            raw_path = data['raw_path']
            artist_list_trimmed.append(artist)
        except KeyError as error:
            print('no match from boilthefrog')
        #print raw_path
        #print type(raw_path)
        # path_length = len(raw_path)

print('artist l', len(artist_list))
print('artist l trimmed', len(artist_list_trimmed))
#with open('artist_list_trimmed.csv', 'wb') as myfile:
    #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerow(mylist)
