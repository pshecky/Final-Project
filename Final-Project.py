import requests
import json
from newsapi import NewsApiClient
from collections import defaultdict
import sqlite3

newsapi = NewsApiClient(api_key='131d9c5b07674440ab948ba13c011d68')

CACHE_FNAME='CNN_data.json'

try:
  cache_file=open(CACHE_FNAME, 'r')
  contents=cache_file.read()
  CACHE_DICTION=json.loads(contents)
  file.close()
except:
  CACHE_DICTION={}

def cache_function(url):
  if url in CACHE_DICTION:
    return CACHE_DICTION[url]
  else:
    all_articles = newsapi.get_everything(q=song, sources='cnn', language='en', sort_by='relevancy')
    CACHE_DICTION[url]=all_articles.text
    dumped_json_cache = json.dumps(CACHE_DICTION) # serialize dictionary to a JSON formatted string 
    fw = open(CACHE_FNAME,"w") # open the cache file
    fw.write(dumped_json_cache) # write the JSON
    fw.close() # Close the open file
    return CACHE_DICTION[url]

def get_CNN_data(d):
    key_words=["music", "song", "top", "chart", "Billboard", "lyrics", "artist", "popular", "songs", "listeners", "pop", "rap", "country", "jazz", "hip-hop", "beat", "EDM", "dance", "radio", "play", "acoustic", "concert", "live"]
    new_d=defaultdict(list)
    for song in d:
      #all_articles = newsapi.get_everything(q=song, sources='cnn', language='en', sort_by='relevancy')
      all_articles=cache_function(song)
      for article in all_articles["articles"]:
        description=article["description"]
        if description is not None:
          for word in description.split():
            if word in key_words:
              id_=article["source"]["id"]
              author=article["author"]
              title=article["title"]
              info=(id_, author, title, description)
              new_d[song].append(info)
      #look in titles too?
          # for word in t.split():
          #   if word in key_words:
          #     id_=article["source"]["id"]
          #     author=article["author"]
          #     title=article["title"]
          #     info=(id_, author, title, description)
          #     new_d[song].append(info)
    return new_d
#di=["Old Town Road", "Hello", "Talk"]
#x=get_CNN_data()
#print(x)



def make_database():
  try:
    conn=sqlite3.connect('CNN.sqlite')
    cur=conn.cursor()
  except:
    print('Could not connect')
  statement='''
  DROP TABLE IF EXISTS 'CNN Articles';
  '''
  cur.execute(statement)
  conn.commit()
  statement= '''
    CREATE TABLE 'CNN Articles'(
      'id_' INTEGER PRIMARY KEY AUTOINCREMENT,
      'song_name' TEXT NOT NULL,
      'article_title' TEXT NOT NULL,
      'article_author' TEXT NOT NULL,
      'article_description' TEXT NOT NULL);
    '''
  cur.execute(statement)
  conn.commit()
  conn.close()

make_database()

def populate_database():
  with open("billboard_cache.json", "r") as read_file:
    data = json.load(read_file)
    n=get_CNN_data(data.keys())
    conn=sqlite3.connect('CNN.sqlite')
    cur=conn.cursor()
    for song in data:
      insertion=(song, data[song][0], data[song][1], data[song][2], data[song][3])
      statement='INSERT INTO "CNN Articles" VALUES (?, ?, ?, ?, ?)'
      cur.execute(statement, insertion)
    conn.commit()




  