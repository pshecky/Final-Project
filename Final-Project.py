# import requests
# import spotipy
# import json
# import spotipy.util as util


# # token=util.prompt_for_user_token(username, scope, client_id="f26fb6698a614b0ea201805fd941995b", client_secret="a7733ad18b9249a986117b97b9b6cafd", redirect_uri="spotify:track:6rqhFgbbKwnb9MLmUQDhG6")
# # spotify=spotipy.Spotify()
# # results=spotify.category_playlists(category_id="top", country="US", limit=20, offset=0)
# # json=results.json()
# # print(json)

# #making request to https://api.spotify.com
# #pulling 100 tracks with popularity ratings from spotify

# r=requests.get("https://api.spotify.com/v1/playlists/playlist_id=37i9dQZEVXbLRQDuF5jeBp/tracks")
# print(r.text)

# #ask about credentials

import requests
import json
from newsapi import NewsApiClient
#my api key for News API
newsapi = NewsApiClient(api_key='131d9c5b07674440ab948ba13c011d68')
#Get all the articles that mention song titles in Peri List from Billboard Charts"
all_articles = newsapi.get_everything(q='song_title',
                                      #sources='bbc-news,the-verge',
                                      #domains='bbc.co.uk,techcrunch.com',
                                      from_param='2019-03-01',
                                      to='2017-03-31',
                                      language='en',
                                      #sort_by='relevancy',
                                      #page=2)

