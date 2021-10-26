from selenium import webdriver
import pandas as pd
import os
import time


driver = webdriver.Chrome(os.getcwd() + "/chromedriver")
driver.get('https://imdb.com')

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