#import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import json
import sqlite3
import re
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

#get base url and initialize Beautiful Soup
url = 'https://www.billboard.com/charts/hot-100/'
def getSoupObjFromURL(url):
    """ return a soup object from the url """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # Line added

    html = urlopen(req, context=ctx).read() # Line modified
    soup = BeautifulSoup(html, "html.parser")
    return soup

soup = getSoupObjFromURL(url)
#create a dictionary of the top 100 charts
#make the key the song title
#and values the artist and ranking on the chart
billboard = {}
lst_of_everything = soup.find_all('div',class_ = 'chart-list-item')
date = soup.find('span', class_="dropdown chart-detail-header__date-selector")
week = date.button.text

for song in lst_of_everything:
    #create a song title variable
    song_info = song.find('div', class_ = 'chart-list-item__title')
    song_title = song_info.span.text
    #create an artist variable
    artist_info = song.find('div', class_ = 'chart-list-item__artist')
    artist = artist_info.text
    #create a ranking variable
    ranking_info = song.find('div', class_ = 'chart-list-item__rank')
    ranking = ranking_info.text
    #add these into the dictionary
    billboard[song_title.strip()] = (artist.strip(), ranking.strip(), week.strip())

print(billboard)

f = open('billboard_cache.json','w')
f.write(json.dumps(billboard))
f.close()


conn = sqlite3.connect('billboard_charts.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Billboard (song TEXT, artist TEXT, ranking INTEGER, week TIMESTAMP)')


for song in billboard.keys():
    song_title = song
    artist_name = billboard[song_title][0]
    rankings = int(billboard[song_title][1])
    date = billboard[song_title][2]
    cur.execute('''INSERT OR IGNORE INTO Billboard (song, artist, ranking, week)
                VALUES (?,?,?,?)''', (song_title,artist_name,rankings, date))


ari_lst = []
for song in billboard.keys():
        if 'Ariana Grande' in billboard[song][0]:
                ari_lst.append(song)

print(len(ari_lst))

post_lst = []
for song in billboard.keys():
        if 'Post Malone' in billboard[song][0]:
                post_lst.append(song)

print(len(post_lst))

billie_lst = []
for song in billboard.keys():
        if 'Billie Eilish' in billboard[song][0]:
                billie_lst.append(song)

print(len(billie_lst))


xvals = ['Ariana Grande', 'Post Malone', 'Billie Eilish']
yvals = [len(ari_lst),len(post_lst),len(billie_lst)]

plt.bar(xvals, yvals, align='center', color= ['pink', 'purple', 'blue'])
#3.Give ylabel to the plot
plt.ylabel("# of Songs in the Hot 100")
#4.Give xlabel to the plot
plt.xlabel("Favorite Artists")
#5.Give the title to the plot
plt.title("How Many Songs Do Our Favorite Artists Have in the Top 100?")
#6.Save the plot as a .png file
plt.savefig('top100.png')

plt.show()


conn.commit()
