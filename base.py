from selenium import webdriver
import pandas as pd
import os
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome(os.getcwd() + "/chromedriver")
driver.get('https://imdb.com')

#   Maximize browser window
driver.maximize_window()

#   Dropdown Variable
dropdown = driver.find_element_by_class_name('ipc-icon--arrow-drop-down')
dropdown.click()
time.sleep(1)

#   Advanced Search Under All (Dropdown Menu)
element = driver.find_element_by_link_text('Advanced Search')
element.click()

#   Get and Click on Advanced Title Search link
advanced_title = driver.find_element_by_link_text('Advanced Title Search')
advanced_title.click()

#   Select feature film checkbox
feature_film = driver.find_element_by_id('title_type-1')
feature_film.click()

#   Select TV movie checkbox
tv_movie = driver.find_element_by_id('title_type-2')
tv_movie.click()

#   Select min release date
min_release_date = driver.find_element_by_name('release_date-min')
min_release_date.click()
min_release_date.send_keys('1990')

#   Select max release date
max_release_date = driver.find_element_by_name('release_date-max')
max_release_date.click()
max_release_date.send_keys('2021')

#   Select min user rating
min_rating = driver.find_element_by_name('user_rating-min')
min_rating.click()
min_rating_dropdown = Select(min_rating)
min_rating_dropdown.select_by_visible_text('1.0')

#   Select max user rating
max_rating = driver.find_element_by_name('user_rating-max')
max_rating.click()
max_rating_dropdown = Select(max_rating)
max_rating_dropdown.select_by_visible_text('10')

#   Oscar Nominated
oscar_nom = driver.find_element_by_id('groups-7')
oscar_nom.click()

#   Select Colors
color = driver.find_element_by_id('colors-1')
color.click()

#   Select Language
language = driver.find_element_by_name('languages')
select_lang = Select(language)
select_lang.select_by_visible_text('English')

#   Select Display Options
dispay_option = driver.find_element_by_id('search-count')
dispay_option.click()
display_dropdown = Select(dispay_option)
display_dropdown.select_by_index(2)

#   Submit button
submit = driver.find_element_by_xpath('(//button[@type="submit"])[2]')
submit.click()

#   Current Url After form submission
current_url = driver.current_url

#   Get Request
response = requests.get(current_url)

#   Status Code
stat_code = response.status_code

#   Soup Object
soup = BeautifulSoup(response.content, 'html.parser')

#Starting point for result items
list_items = soup.find_all('div', {'class': 'lister-item'}) 

#   Movie title
title = [result.find('h3').find('a').get_text() for result in list_items]

#   Movie Year
year = [result.find('h3').find('span', {'class': 'lister-item-year'}).get_text().replace('(', '').replace(')', '') for result in list_items]

#   Duration
duration = [result.find('span', {'class': 'runtime'}).get_text() for result in list_items]

#   Genre
genre = [result.find('span', {'class': 'genre'}).get_text().strip() for result in list_items]

#   Rating
rating = [result.find('div', {'class', 'ratings-imdb-rating'}).get_text().strip() for result in list_items]

imdb_data = pd.DataFrame({
    'Movie Title': title,
    'Movie Year': year,
    'Movie Duration': duration,
    'Movie Genre': genre,
    'Movie Rating': rating
    })

