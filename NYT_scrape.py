# from urllib.request import Request
# from urllib.request import urlopen
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# import requests
# import json
# import sqlite3
# import re
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import json
# import os

# #get base url and initialize Beautiful Soup
# url = 'https://www.nytimes.com/section/arts/music'
# def getSoupObjFromURL(url):
#     """ return a soup object from the url """
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE

#     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # Line added

#     html = urlopen(req, context=ctx).read() # Line modified
#     soup = BeautifulSoup(html, "html.parser")
#     return soup

# soup = getSoupObjFromURL(url)

#     # create a dictionary of the 100 most recent articles about music from NYT music section
#     # with the key being the article title 
#     # and value being the description

# def scrape(soup):

#     NYT = {}
#     lst_of_everything = soup.find('section',id = 'stream-panel', class_="css-1wn7afn")
#     lst_of_articles=lst_of_everything.find('div', class_='css-13mho3u')
#     articles=lst_of_articles.find('ol')
#     for article in articles:
#         n=article.find('div', class_='css-1cp3ece')
#         info=n.find('div', class_='css-4jyr1y')
#         title=info.find('h2', class_='css-1dq8tca e1xfvim30')
#         title_name=title.text

#         # #create a date variable:
#         description_info=article.find("p", class_="css-1echdzn e1xfvim31")
#         description=description_info.text
        
#         #add these into the dictionary
#         NYT[title_name] = [description]
# show_more=soup.find("div", class_="css-12pz3n5")
# print(show_more.text)
#     # for extra in 
#     # #print(NYT)
#     # print(NYT)

# scrape(soup)

# f = open('NYT_cache.json','w')
# f.write(json.dumps(scrape(soup)))
# f.close()

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
url = 'https://www.nytimes.com/column/popcast-pop-music-podcast'
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

    # create a dictionary of the 100 most recent articles about music from NYT music section
    # with the key being the article title 
    # and value being the description

def scrape(soup):
    
    NYT = {}
    article_lst_1=[]
    lst_of_everything = soup.find("section", id="collection-popcast-pop-music-podcast", class_="popcast-pop-music-podcast-collection collection", itemscope="", itemtype="http://schema.org/CollectionPage")
    lst_of_articles=lst_of_everything.find("div", class_="stream-supplemental")
    articles=lst_of_articles.find("div", id="main-tabs", class_="main-tabs tabs")
    a=articles.find("ol", class_="story-menu theme-stream initial-set")
    title=a.split()
    #print(a.text.strip())
    article_lst_1.append(a.text.strip())
    print(article_lst_1)
    #data=a.find("article", class_='story theme-summary', itemscope="", itemtype="http://schema.org/NewsArticle")


    #print(articles.text)
    #NYT.append(articles)


    #n=articles.find("ol", id="story-menu-additional-set-latest", class_="story-menu theme-stream additional-set hidden")
    #print(n.text)


    #lst_of_articles=lst_of_everything.find('div', class_='css-13mho3u')
#     articles=lst_of_articles.find('ol')
#     for article in articles:
#         n=article.find('div', class_='css-1cp3ece')
#         info=n.find('div', class_='css-4jyr1y')
#         title=info.find('h2', class_='css-1dq8tca e1xfvim30')
#         title_name=title.text

#         # #create a date variable:
#         description_info=article.find("p", class_="css-1echdzn e1xfvim31")
#         description=description_info.text
        
#         #add these into the dictionary
#         NYT[title_name] = [description]
# show_more=soup.find("div", class_="css-12pz3n5")
# print(show_more.text)
#     # for extra in 
#     # #print(NYT)
#     # print(NYT)

scrape(soup)