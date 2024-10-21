# using the Spotipy library 
# 1. authenticate (log in)
# 2. constent data stream (reading of it)
# 3. search for songs and retrieve URLs
# 4. add songs to queue
# 5. be able to return the queue
# 6. delete from queue
# functions:
# queue() -> gets the current user's queue 
# add_to_queue() -> takes song URL and adds it to the queue

import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from pprint import pprint
import random

     

#"log in"


# connected to Anuj's spotify account now 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="142b6b91ca9c4fff8492e3e562cfcc3d",
                                               client_secret="6093e73128bf48f9bbcab1288cc531c0",
                                               redirect_uri="http://localhost/8000",
                                               scope="user-library-read,user-library-read,user-read-recently-played,user-read-currently-playing,user-read-playback-state,user-modify-playback-state"))
print(sp.me()['uri'])
#track_uri = "spotify:track:YOUR_TRACK_URI"
#sp.add_to_queue(track_uri)
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

users_queue = sp.queue()

currently_playing_track_or_episode = users_queue['currently_playing']
if not currently_playing_track_or_episode == None:
    print(f"Currently playing: {currently_playing_track_or_episode['name']}")


for track_or_episode in users_queue['queue']:
    print(f"Queued: {track_or_episode['name']}")

#sp.current_playback()
#devices = sp.devices()
#print(devices)

def search_song():
    print("what song?")
    name = input()
    result = sp.search(name)

    # first thing to pop up 
    # return top 10 songs when 
    print(result['tracks'])
    print(result['tracks']['items'][0]['name'])
    uri = result['tracks']['items'][0]['uri']
    return uri

# returns top 10 songs after a search
def search_list():
    name = input()
    result = sp.search(name)
    song_list = []
    # maybe a dictionary with name
    #print(result['tracks']['items'][4]['name'])
    for i in range(0,10):
        song_list.append(result['tracks']['items'][i]['name'] + " by ")
    print(song_list)
    


    


#def add_to_queue(uri):


#def rem_from_queue(uri):


# main
#while(true):
    # read in inputs

    #If input === 
uri_song = search_song()
print(uri_song)
sp.add_to_queue(uri_song, None)

#search_list()

#sp.me()['uri'] = '' # did not do anything 

