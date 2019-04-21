import requests
import json
from newsapi import NewsApiClient
from collections import defaultdict
import sqlite3
from collections import defaultdict
newsapi = NewsApiClient(api_key='cc15faf004db46cfabdf18bc77c8a9e5')

with open("billboard_cache.json", "r") as read_file:
    data = json.load(read_file)

def get_abc_data(n):
    ABC=defaultdict(list)
    for song in n:
        key_words=["music", "song", "chart", "Billboard", "lyrics", "artist", "songs", "pop", "rap", "country", "jazz", "hip-hop", "EDM", "radio", "acoustic", "concert",  "Coachella", "concerts",  "Youtube", "Spotify", "iTunes", "Soundcloud", "genre", "grammy"]
        all_articles = newsapi.get_everything(q='song', sources='abc-news', domains='https://abcnews.go.com', sort_by='relevancy')
        for article in all_articles['articles']:
            description=article['description']
            if description is not None:
                for word in description.split():
                    if word in key_words:
                        author=article["author"]
                        title=article["title"]
                        info=(author, title)
                        ABC[song.strip()].append(info)

    return ABC
get_abc_data(data)

f = open('ABC_cache.json','w')
f.write(json.dumps(get_abc_data(data)))
f.close()

def make_database():
    try:
        conn=sqlite3.connect('CNN.sqlite')
        cur=conn.cursor()
    except:
        print('Could not connect')
    statement='''
    DROP TABLE IF EXISTS 'ABC';
    '''
    cur.execute(statement)
    conn.commit()
    statement= '''CREATE TABLE 'ABC' (song TEXT NOT NULL, author TEXT NOT NULL, title TEXT NOT NULL)'''
    cur.execute(statement)
    conn.commit()
    conn.close()

make_database()

def populate_database():
    conn=sqlite3.connect('CNN.sqlite')
    cur=conn.cursor()
    for song in get_abc_data(data.keys()):
        song_title=song
        for l in get_abc_data(data)[song_title]:
        #print(song_title_from_Billboards)
        #id_=str(get_abc_data(data)[song_title_from_Billboards][0])
        #print(id_)
            author=get_abc_data(data)[song_title][0]
        #print(author)
            title=get_abc_data(data)[song_title][1]
        #print(title)
        #description=get_abc_data(data)[song_title][0]
        
        #print(description)
            cur.execute('''INSERT OR IGNORE INTO 'ABC' (song, author, title) VALUES (?,?,?)''', (song_title, author, title))
    conn.commit()
populate_database()