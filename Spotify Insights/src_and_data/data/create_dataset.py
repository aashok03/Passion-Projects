import sys
import spotipy
import spotipy.util as util
import os
import numpy as np
import pandas as pd

#Set Environment Variables
os.environ["SPOTIPY_CLIENT_ID"] ='2155261afe5e459c9ea0c826f0a51f12'
os.environ["SPOTIPY_CLIENT_SECRET"] ='7ae6d49468594c548805240548432d9c'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://example.com'

username = "Athokshay Ashok"
scope = "user-read-currently-playing"

SPOTIPY_CLIENT_ID ='2155261afe5e459c9ea0c826f0a51f12'
SPOTIPY_CLIENT_SECRET ='7ae6d49468594c548805240548432d9c'
SPOTIPY_REDIRECT_URI = 'http://example.com'

#Connect to Spotipy
token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

#Read in names and IDs of top 20-30 artists
top_30 = pd.read_csv('top_30_artists_2019.csv')
top_30.columns = ["artist", "id"]
top_30_artist = list(top_30.artist)
top_30_id = list(top_30.id)

print(top_30_artist)

#Open files for song features and song popularity data
f = open("x.csv", "a", encoding='utf-8')
g = open("y.csv", "a", encoding='utf-8')
f.write("artist,track_name,track_id,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,duration_ms,explicit\n")
g.write("popularity\n")


#Given a Spotpy artist ID, this function returns a list of all the tracks that
#the artist has released in the form of their Sptify IDs
def get_artist_all_songs(artist_id):

	artist_all_songs_id = list()

	artist_items = sp.artist_albums(artist_id)['items']
	for i in range (len(artist_items)):
		album_id = artist_items[i]['id']
		album_items = sp.album_tracks(album_id)['items']
		for j in range (len(album_items)):
			artist_all_songs_id.append(album_items[j]['id'])

	return list(set(artist_all_songs_id))


#Write song feature data and popularity data for all the songs made by the
#top 20-30 artists to two separate files
for i in range (len(top_30_id)):
	artist_all_songs_id = get_artist_all_songs(top_30_id[i])
	
	for j in range (len(artist_all_songs_id)):
		song_features = sp.audio_features(artist_all_songs_id[j])[0]
		song = sp.track(artist_all_songs_id[j])		

		if song_features is None:
			break

		f.write(top_30_artist[i] + ",")
		f.write(song['name'].replace(",", " ") + ",")
		f.write(str(song_features['id']) + ",")
		f.write(str(song_features['danceability']) + ",")
		f.write(str(song_features['energy']) + ",")
		f.write(str(song_features['key']) + ",")
		f.write(str(song_features['loudness']) + ",")
		f.write(str(song_features['mode']) + ",")
		f.write(str(song_features['speechiness']) + ",")
		f.write(str(song_features['acousticness']) + ",")
		f.write(str(song_features['instrumentalness']) + ",")
		f.write(str(song_features['liveness']) + ",")
		f.write(str(song_features['valence']) + ",")
		f.write(str(song_features['duration_ms']) + ",")

		if song['explicit'] == True:
			f.write("1\n")
		else:
			f.write("0\n")

		g.write(str(song['popularity']) + "\n")

		print(song['name'])

	print("\n\n")