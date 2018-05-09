# from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time
# from config  import Config
# import webbrowser
# from .server import block_until_token
from utils import *
import urllib
raw_csv =  pd.read_csv('/Users/aaronopp/Desktop/GOOD_MEDIA/hackathon_extras/events_final.csv')
# with open("/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/aaronopp.txt", "rb") as fp:   # Unpickling
#     user_artists = pickle.load(fp)

# user_artists = ['Roosevelt', 'Lorde', 'Camila Cabello', 'Francis and the Lights']

user_artists = ['Drake', 'SALES', 'slenderbodies', 'TV Girl', 'The Avalanches', 'King Gizzard & The Lizard Wizard', 'Made in Heights', 'eevee', 'FKJ', 'Beach Fossils', 'Good Morning',  'Christopher Owens']
with open('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/app/artist_list_trimmed_final.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    artist_list_3_15_f = your_list[0]


lowest_matches_dict = get_lowest_artist_matches(user_artists[4:], artist_list_3_15_f)

predicted_artists = []
for value in lowest_matches_dict:
    predicted_artists.append(value['SXSW_artist'])

predicted_artists = set(list(predicted_artists))
print('DONE', predicted_artists)

with open("philip.txt", "wb") as fp:   #Pickling
    pickle.dump(predicted_artists, fp)

for artist in predicted_artists:
    m = find_artist_info(raw_csv, artist)  
    #print m