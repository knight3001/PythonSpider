#!/usr/bin/env python
# encoding=utf-8
# pylint: disable=C0103,C0111
import requests
from bs4 import BeautifulSoup

def main():
    ls = ""
    #url = "http://www.babynamewizard.com/name-list/australian-boys-names-most-popular-names-for-boys-in-australia-new-south-wales"
    url = "http://www.babynamewizard.com/name-list/australian-girls-names-most-popular-names-for-girls-in-australia-new-south-wales"
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    list_soup = soup.find('ol', attrs={'class':'no-icon'})
    for li in list_soup.find_all('li'):
        try:
            name = li.find('a').get_text()
        except AttributeError:
            name = li.get_text()
        ls += "'" + name + "',"
    print(ls)

if __name__ == '__main__':
    main()