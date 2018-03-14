import sys
import spotipy
import spotipy.util as util
import time as time
import pickle
import urllib
import urllib.parse, urllib.request

import webbrowser
from .server import block_until_token

import urllib.request, urllib.parse, urllib.error, json
import csv
import pandas as pd


def get_path_length(user_artist, sxsw_artist, url):
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
    return path_length, f


def save_obj(obj, name ):
    with open('data/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('data/' + name + '.pkl', 'rb+') as f:
        return pickle.load(f)

def get_lowest_artist_matches(user_artists_short, artist_list_3_15_f):
    url = "http://smarterplaylists.playlistmachinery.com/frog/path";

    start = time.time()

    lowest_matches_dict = []
    for user_artist in user_artists_short:
        lowest_path_length = 15
        for artist in artist_list_3_15_f:

            f = { 'src' : user_artist, 'dest' : artist}
            url_encoded = urllib.parse.urlencode(f)
            full_url = url + '?' + url_encoded
            # print full_url
            response = urllib.request.urlopen(full_url)
            data = json.loads(response.read())
            try:
                raw_path = data['raw_path']
            except KeyError as error:
                print('no match from boilthefrog')

            path_length = len(raw_path)
            if path_length == 5:
                lowest_match = f
                # print path_length
                lowest_path_length = path_length
                break
            if path_length < lowest_path_length:

                lowest_match = f
                lowest_path_length = path_length

        print('the lowest per your spotify top artist')
        print(lowest_path_length)
        print(lowest_match)
        lowest_matches_dict.append({"spotify_artist": lowest_match['src'], "SXSW_artist": lowest_match['dest'], "path_length": lowest_path_length})

        print(lowest_matches_dict)
    print('took') 
    print(time.time() - start)
    return lowest_matches_dict