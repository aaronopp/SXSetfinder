from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm, SpotifyForm

import sys
import spotipy
import spotipy.util as util
import time as time

import webbrowser
from server import block_until_token
from utils import *

user_artists = {0: 'Kendrick Lamar', 1: 'Kanye West', 2: 'John Mayer', 3: 'The Strokes', 4: 'Tame Impala', 5: 'The Undercover Dream Lovers', 6:'ZHU', 7:'Portugal. The Man', 
8:'Jay Chou', 9:'Taylor Swift', 10:'Spoon'
}
print user_artists
print type(user_artists)

SXSW_artists = ['070 Shake', '16 the Olympus', '1982', '1kPhew', '1Playy' , "20 Somethin' Band/Tenth Child Inc. House Band", '24Hrs', '3 Hand Stephen', '5ive', '6Blocc', '90 One', 'A-RON', 'Aaron Lee Tasjan']

