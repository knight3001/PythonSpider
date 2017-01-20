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
        quote = ""
        if quote_div:
            quote = quote_div.find('span', attrs={'class':'inq'}).get_text()
        link = bt_login(movie_name)

        movie = {"name":movie_name,
                 "pic":pic,
                 "star":star,
                 "quote":quote,
                 "link":link,
                 "date":datetime.datetime.utcnow()}
        movie_id = movies.insert_one(movie).inserted_id
        #movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class':'next'}).find('a')
    if next_page:
        return DOWNLOAD_URL + next_page['href']

    return None

def bt_login(moviename):
    links = []

    s = requests.session()
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                      '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Host': 'www.bttt99.com',
    }
    data = {
        'show': 'title,ftitle,type,area,time,director,player,actor,imdb',
        'tbname': 'movie',
        'tempid': '1',
        'keyboard': moviename
    }
    resp = s.post('http://www.bttt99.com/e/search/', headers=headers, data=data)
    soup = BeautifulSoup(resp.text, "html.parser")

    try:
        linkFull = soup.find('div', attrs={'class':'item cl'}). \
               find('p', attrs={'class':'tt cl'}).find('a')['href']
        linkFirst = linkFull.split("http://www.bttt99.com/v/")
        if len(linkFirst) > 1:
            linkId = linkFirst[1].split("/")[0]
        else:
            linkId = linkFull.split("/v/")[1].split("/")[0]
        if linkId:
            headers['Referer'] = 'http://www.bttt99.com/v/' + str(linkId) + '/'
            link_resp = s.get('http://www.bttt99.com/e/show.php?classid=1&id=' \
                        + linkId, headers=headers)
            link_soup = BeautifulSoup(link_resp.text, "html.parser")
            magnet_links = link_soup.find_all('li')

            for magnet in magnet_links:
                lk = magnet.find('a')
                if lk:
                    title = magnet.find('a')['title'].replace(moviename, "").strip()
                    href = magnet.find('a')['href']
                    links.append({"title":title, "href":href})
    except AttributeError as e:
        print(moviename + " " + str(e))
    except IndexError as e:
        print(moviename + " " + str(e))
    return links

def main():
    """
    movies = startDB()
    for movie in movies.find():
        movie_name = movie['name']
        links = bt_login(movie_name)
        movie['link'] = links
        movies.save(movie)
    """
    url = DOWNLOAD_URL
    movies = startDB()
    #with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
    while url:
        html = download_page(url)
        url = parse_html(html, movies)
        #fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
    print("done")

if __name__ == '__main__':
    main()
