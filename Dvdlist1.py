#!//usr/bin/env python3
#created: 25/07/2019

from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd"

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html5lib')

for movie in soup.find_all('div',{'class':'lister-item-content'}):
    rank = movie.find('span').contents[0]
    title = movie.find('h3',{'class':'lister-item-header'}, 'a').contents[3].contents[0]
    year = movie.find('h3', {'class':'lister-item-header'}, 'span').contents[5].contents[0]
    rating = movie.find('p', {'class':'text-muted text-small'}, 'certificate').contents[1].contents[0]

    print(rank, title, year, rating)
