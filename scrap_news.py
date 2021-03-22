import requests
from bs4 import BeautifulSoup
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

browser = webdriver.Chrome('./chromedriver')
URL = 'https://coinmarketcap.com/headlines/news/'

browser.get(URL)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 1

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns-=1


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all("div", {"class": "uikit-row"})


parsed_data = []

for job_elem in results[1:]:
    title_elem = job_elem.find('a', class_='sc-AxhUy giWqzT cmc-link')
    text_elem = job_elem.find('p', class_='sc-AxhUy ktwnrO')
    time_elem = job_elem.find('span', class_='sc-1j9kn84-0 iIITVL')

    parsed_data.append([str(title_elem.text), str(text_elem.text), str(time_elem.text)])

    title_string = str(title_elem.text)
    blob_title = TextBlob(title_string, analyzer=NaiveBayesAnalyzer())
    analysis_title = blob_title.sentiment
    print(title_elem.text)
    print(analysis_title)

    text_string = str(text_elem.text)
    blob_text = TextBlob(text_string, analyzer=NaiveBayesAnalyzer())
    analysis_text = blob_text.sentiment.classification
    print(analysis_text)

    print()



