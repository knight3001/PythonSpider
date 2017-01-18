#!/usr/bin/env python
# encoding=utf-8
# pylint: disable=C0103,C0111

import codecs
import datetime
import sys
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


DOWNLOAD_URL = "http://movie.douban.com/top250"


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    data = requests.get(url, headers=headers).content
    return data

def startDB():
    client = MongoClient('localhost', 27017)
    db = client['PythonSpider']
    collection = db['Movies']
    return collection

def parse_html(html, movies):
    soup = BeautifulSoup(html, "html.parser")
    movie_list_soup = soup.find('ol', attrs={'class':'grid_view'})

    #movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        pic = movie_li.find('div', attrs={'class':'pic'}).find('a').find('img')['src']
        detail = movie_li.find('div', attrs={'class':'info'})
        movie_name = detail.find('div', attrs={'class':'hd'}) \
                           .find('span', attrs={'class':'title'}).get_text()
        star = detail.find('div', attrs={'class':'bd'}).find('div', attrs={'class':'star'}) \
                     .find('span', attrs={'class':'rating_num'}).get_text()
        quote_div = detail.find('div', attrs={'class':'bd'}).find('p', attrs={'class':'quote'})
        if quote_div:
            quote = quote_div.find('span', attrs={'class':'inq'}).get_text()
        movie = {"name":movie_name,
                 "pic":pic,
                 "star":star,
                 "quote":quote,
                 "date":datetime.datetime.utcnow()}
        movie_id = movies.insert_one(movie).inserted_id
        #movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class':'next'}).find('a')
    if next_page:
        return DOWNLOAD_URL + next_page['href']

    return None

def main():
    url = DOWNLOAD_URL
    movies = startDB()
    #with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
    while url:
        html = download_page(url)
        url = parse_html(html, movies)
        #fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
    """
    movies = startDB()
    for post in movies.find():
        print(post["pic"])
    """



if __name__ == '__main__':
    main()
