import requests
from bs4 import BeautifulSoup

base_search_url = 'https://www.imdb.com/find?q={}'

is_movie_exists = False

while not is_movie_exists:
    movie_name_input = input('Please enter the movie name : ')
    movie_name_words = movie_name_input.split(' ')
    movie_name = ''
    if len(movie_name_words) < 1 : 
        movie_name = movie_name_words[0]
    else:
        movie_name = '+'.join(movie_name_words)

    movie_name = movie_name.lower()
    movie_search_url = base_search_url.format(movie_name)
    movie_search_response = requests.get(movie_search_url)


    movie_search_soup = BeautifulSoup(movie_search_response.text, "html.parser")

    if movie_search_soup.find_all("div", {"class": "findNoResults"}):
        is_movie_exists = False
    else :
        is_movie_exists = True

base_movie_url = 'https://www.imdb.com{}'
movie_path = movie_search_soup.select('.findList')[0].select('a')[0]['href']


url = base_movie_url.format(movie_path)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.select('.ipc-page-section > div')[1].select('div')[0]
title = items.select('h1')[0].text
details_div = items.select('div')[0]
details_list = details_div.select('ul')[0]

year_li = details_list.select('li')[0]
year = year_li.select('span')[0].text

censor_rating_li = details_list.select('li')[1]
censor_rating = censor_rating_li.select('span')[0].text

duration = details_list.select('li')[2].text

rating_wrapper = soup.select('.ipc-button__text > div')[0].select('div')[1]
rating = rating_wrapper.select('div')[0].select('span')[0].text
total_ratings_given = rating_wrapper.select('div')[2].text

cast_list = []
cast_wrapper = soup.select('.title-cast--movie > div')[1].select('div')[1]

for c in cast_wrapper:
    cast_list.append(c.select('div')[1].select('a')[0]['aria-label'])

print('Movie Name : ', title)
print('Movie Year : ', year)
print('Movie Duration : ', duration)
print('Movie Censor Rating : ', censor_rating)
print('Movie Rating : ', rating)
print('Movie Total Ratings : ', total_ratings_given)
print('Movie Cast : ', cast_list)
    

