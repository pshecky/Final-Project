import requests
import spotipy
import json
import spotipy.util as util


token=util.prompt_for_user_token(username, scope, client_id="f26fb6698a614b0ea201805fd941995b", client_secret="a7733ad18b9249a986117b97b9b6cafd", redirect_uri="spotify:track:6rqhFgbbKwnb9MLmUQDhG6")
spotify=spotipy.Spotify()
results=spotify.category_playlists(category_id="top", country="US", limit=20, offset=0)
json=results.json()
print(json)

#making request to https://api.spotify.com
#pulling 100 tracks with popularity ratings from spotify

