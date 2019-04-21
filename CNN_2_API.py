import requests
import json
from newsapi import NewsApiClient
from collections import defaultdict
import sqlite3
newsapi = NewsApiClient(api_key='131d9c5b07674440ab948ba13c011d68')

# def get_CNN_data(d):
#   key_words=["music", "song", "top", "chart", "Billboard", "lyrics", "artist", "popular", "songs", "listeners", "pop", "rap", "country", "jazz", "hip-hop", "beat", "EDM", "dance", "radio", "play", "acoustic", "concert", "live"]
#   new_d=defaultdict(list)
#   for song in d.keys():
#     all_articles = newsapi.get_everything(q=song, sources='cnn', language='en', sort_by='relevancy')
#     for article in all_articles["articles"]:
#       description=article["description"]
#       print(description)
#       if description is not None:
#         for word in description.split():
#           if word in key_words:
#             id_=article["source"]["id"]
#             print(id_)
#             author=article["author"]
#             print(author)
#             title=article["title"]
#             print(title)
#             info=(id_, author, title, description)
#             print(info)
#             new_d[song].append(info)
#     print(new_d)
#     return new_d

# di={"Old Town Road, Wow., 7 rings"}
# get_CNN_data(di)


# # def make_database():
# #   try:
# #     conn=sqlite3.connect('CNN.sqlite')
# #     cur=conn.cursor()
# #   except:
# #     print('Could not connect')
# #   statement='''
# #   DROP TABLE IF EXISTS 'CNN Articles';
# #   '''
# #   cur.execute(statement)
# #   conn.commit()
# #   statement= '''
# #     CREATE TABLE 'CNN Articles'(
# #       id_ TEXT NOT NULL,
# #       song_name TEXT NOT NULL,
# #       article_title TEXT NOT NULL,
# #       article_author TEXT NOT NULL,
# #       article_description TEXT NOT NULL)
# #     '''
# #   cur.execute(statement)
# #   conn.commit()
# #   conn.close()
# # make_database()

# # def populate_database():
# #   with open("billboard_cache.json", "r") as read_file:
# #     data = json.load(read_file)
# #     n = get_CNN_data(data)
# #     conn=sqlite3.connect('CNN.sqlite')
# #     cur=conn.cursor()
# #     for song in n.keys():
# #       print(str(n[song][0]))
# #       print(str(song))
# #       print(str(n[song][2]))
# #       print(str(n[song][1]))
# #       print(str(n[song][3]))

#       insertion=(str(n[song][0]), str(song), str(n[song][2]), str(n[song][1]), str(n[song][3]))
#       #try printing out these insertions individually to make sure it is the right stuff FIRST
#       #problem was definitley with the insertion statements before
#       statement='''INSERT OR IGNORE INTO "CNN Articles" VALUES (?, ?, ?, ?, ?)'''
#       #cur.execute(statement, insertion)
#     #conn.commit()
# #populate_database()

import requests
import json
from newsapi import NewsApiClient
from collections import defaultdict
import sqlite3
newsapi = NewsApiClient(api_key='131d9c5b07674440ab948ba13c011d68')


with open("billboard_cache.json", "r") as read_file:
    data = json.load(read_file)

def get_CNN_data(n):
    CNN=defaultdict(list)
    for song in n:
        key_words=["music", "song", "chart", "Billboard", "lyrics", "artist", "songs", "pop", "rap", "country", "jazz", "hip-hop", "EDM", "radio", "acoustic", "concert",  "Coachella", "concerts",  "Youtube", "Spotify", "iTunes", "Soundcloud", "genre", "grammy"]
        all_articles = newsapi.get_everything(q='song', domains='https://www.cnn.com/entertainment', sort_by='relevancy')
        for article in all_articles['articles']:
            description=article['description']
            if description is not None:
                for word in description.split():
                    if word in key_words:
                        author=article["author"]
                        title=article["title"]
                        info=(author, title)
                        CNN[song.strip()].append(info)

    return CNN
get_CNN_data(data)

f = open('CNN_cache.json','w')
f.write(json.dumps(get_CNN_data(data)))
f.close()

def make_database():
    try:
        conn=sqlite3.connect('CNN.sqlite')
        cur=conn.cursor()
    except:
        print('Could not connect')
    statement='''
    DROP TABLE IF EXISTS 'CNN';
    '''
    cur.execute(statement)
    conn.commit()
    statement= '''CREATE TABLE 'CNN' (song TEXT NOT NULL, author TEXT NOT NULL, title TEXT NOT NULL)'''
    cur.execute(statement)
    conn.commit()
    conn.close()

make_database()

def populate_database():
    conn=sqlite3.connect('CNN.sqlite')
    cur=conn.cursor()
    for song in get_CNN_data(data.keys()):
        song_title=song
        for song in get_CNN_data(data)[song_title]:
            #print(song)
        #print(song_title_from_Billboards)
        #id_=str(get_abc_data(data)[song_title_from_Billboards][0])
        #print(id_)
            author=song[0]
            #print(author)
        #print(author)
            title=song[1]
            #print(title)
        #print(title)
        #description=get_abc_data(data)[song_title][0]
        
        #print(description)
        cur.execute('''INSERT OR IGNORE INTO 'CNN' (song, author, title) VALUES (?,?,?)''', (song_title, author, title))
    conn.commit()
populate_database()

