#!//usr/bin/env python3
#created: 27/07/2019
#appended: 27/11/2019

from bs4 import BeautifulSoup
import requests
import os

os.system('clear')

url = "https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd"

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html5lib')
title = soup.find('h1').contents[0]
update = soup.find('span',{'id':'list-overview-lastupdated'}).contents[0]

print(title)
print(update)

for movie in soup.find_all('div',{'class':'lister-item-content'}):
    
    rank = movie.find('span').contents[0]
    
    movieTitle = movie.find('h3',{'class':'lister-item-header'}, 'a').contents[3].contents[0]
    
    year = movie.find('h3', {'class':'lister-item-header'}, 'span').contents[5].contents[0]
    
    rating = movie.find('p', {'class':'text-muted text-small'}, 'certificate').contents[1].contents[0]
    
    star = movie.find('div',{'class':'ipl-rating-star small'}, 'span').contents[3].contents[0]
    
    genre = movie.find('span',{'class':'genre'}).contents[0]
    
    discription = movie.find('p', {'class':''}).get_text()

    runtime = movie.find('span', {'class':'runtime'}).get_text()

    print('#'*60)
    print(rank, movieTitle, year, rating)
    print(runtime)
    print(genre)
    print('rating:',star)
    print(discription)
