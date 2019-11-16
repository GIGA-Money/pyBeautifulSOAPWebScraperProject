# import libraries
# using site https://www.planetside-universe.com/leaderboard.php?server=Emerald
# info site https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
from selenium import webdriver
import time
import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# specify the url
urlpage = 'https://www.planetside-universe.com/leaderboard.php?server=Emerald&page=0'
hdr = {'User-Agent': 'Mozilla/5.0'}
context = ssl._create_unverified_context()
req = Request(urlpage, headers=hdr)
page = urlopen(req, context=context)
print(urlpage)
# query the website and return the html to the variable 'page'
driver = webdriver.Firefox(executable_path = 'D:/School/Fall 19/adv db/geckodriver-v0.26.0-win64')
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# updated Nov 2019:
results = soup.find_all('div', attrs={'class': 'co-product'})
print('Number of results', len(results))