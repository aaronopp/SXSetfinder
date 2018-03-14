import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
from server import block_until_token
from utils import *

import urllib, json
import csv
import pandas as pd


def get_path_length(user_artist, sxsw_artist, url):
    f = { 'src' : user_artist, 'dest' : sxsw_artist}
    # f = { 'src' : 'Kendrick Lamar', 'dest' : '1982'}
    url_encoded = urllib.urlencode(f)
    full_url = url + '?' + url_encoded
    # print full_url
    response = urllib.urlopen(full_url)
    data = json.loads(response.read())
    try:
        raw_path = data['raw_path']
    except KeyError as error:
        print 'no match from boilthefrog'
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

