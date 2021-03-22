from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

facebookusername = ''
facebookpassword = ''


browser = webdriver.Chrome()
browser.get('http://www.facebook.com')

browser.find_element_by_xpath('//*[@id="email"]').send_keys(facebookusername)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys(facebookpassword)
browser.find_element_by_xpath('//*[@id="u_0_b"]').send_keys(Keys.RETURN)

time.sleep(5)

url=browser.get('https://www.facebook.com/groups/no.experience')

time.sleep(3)

# function to handle dynamic page content loading - using Selenium
def fb_scroller(browser):
    # define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        blogxtract()
        # define how many seconds to wait while dynamic page content loads
        time.sleep(3)
        newHeight = browser.execute_script("return document.body.scrollHeight")

        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight

    return browser


def pageRefresh():
    x=0
    for x in range(4):
        x +=1
        browser.refresh()
        time.sleep(3)
        if x == 4:
            break

def blogxtract():

    soup = BeautifulSoup(browser.page_source, "html.parser")
    results = soup.findAll('div', {'class': "dati1w0a"})
    print(soup)
    try:
            for result in results:

              print(result.get_text())
    # error handling
    except (AttributeError, TypeError, ValueError):
        print
        "missing_value"


pageRefresh()
fb_scroller(browser)
