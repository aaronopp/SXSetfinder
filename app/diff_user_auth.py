import spotipy
import spotipy.oauth2 as oauth2
import sys

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

#cope = 'user-read-playback-state user-read-recently-played'
#sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id='dbe2a20785304190b8e35d5d6644397b', 
    #client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:5555/redirect',  scope=scope)
#print('sp oauth', sp_oauth)
def generate_token():
    credentials = oauth2.SpotifyClientCredentials(
        client_id='dbe2a20785304190b8e35d5d6644397b',
        client_secret='d73cf4a1525c44e899feeeff4b840040')
    token = credentials.get_access_token()
    return token


def get_playlists(username):
    playlists = spotify.user_playlists(username)
    check = 1

    while True:
        for playlist in playlists['items']:
            # in rare cases, playlists may not be found, so playlists['next']
            # is None. Skip these.
            if playlist['name'] is not None:
                print('')
                print('playlist:')
                playlist_title = playlist['name'] + ' - ' + str(playlist['tracks']['total'])
                playlist_title += ' tracks'
                print(playlist_title)
                show_playlist(playlist)
                check += 1
        if playlists['next']:
            playlists = spotify.next(playlists)
        else:
            break


def show_playlist(playlist):
    results = spotify.user_playlist(
        playlist['owner']['id'], playlist['id'], fields='tracks,next')

    tracks = results['tracks']
    show_tracks(tracks)


def show_tracks(tracks):
    n = 1
    while True:
        for item in tracks['items']:
            track = item['track']
            track_title = str(n) + '. '
            track_title += track['name'] + ' - ' + track['artists'][0]['name']
            print(track_title)
            n += 1
        # 1 page = 50 results
        # check if there are more pages
        if tracks['next']:
            tracks = spotify.next(tracks)
        else:
            break

token = generate_token()
spotify = spotipy.Spotify(auth=token)
get_playlists(username)