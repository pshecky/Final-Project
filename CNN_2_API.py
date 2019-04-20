import requests
import json
from newsapi import NewsApiClient
from collections import defaultdict
import sqlite3
newsapi = NewsApiClient(api_key='131d9c5b07674440ab948ba13c011d68')
def get_CNN_data(d):
  key_words=["music", "song", "top", "chart", "Billboard", "lyrics", "artist", "popular", "songs", "listeners", "pop", "rap", "country", "jazz", "hip-hop", "beat", "EDM", "dance", "radio", "play", "acoustic", "concert", "live"]
  new_d=defaultdict(list)
  for song in d.keys():
    all_articles = newsapi.get_everything(q=song, sources='cnn', language='en', sort_by='relevancy')
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
  return new_d

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
      id_ TEXT NOT NULL,
      song_name TEXT NOT NULL,
      article_title TEXT NOT NULL,
      article_author TEXT NOT NULL,
      article_description TEXT NOT NULL)
    '''
  cur.execute(statement)
  conn.commit()
  conn.close()
make_database()

def populate_database():
  with open("billboard_cache.json", "r") as read_file:
    data = json.load(read_file)
    n = get_CNN_data(data)
    conn=sqlite3.connect('CNN.sqlite')
    cur=conn.cursor()
    for song in n.keys():
      insertion=(str(song), str(n[song][0]), str(n[song][1]), str(n[song][2]), str(n[song][3]))
      #try printing out these insertions individually to make sure it is the right stuff FIRST
      statement='''INSERT OR IGNORE INTO "CNN Articles" VALUES (?, ?, ?, ?)'''
      cur.execute(statement, insertion)
    conn.commit()
populate_database()




  