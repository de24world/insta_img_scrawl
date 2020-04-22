# install module
# sudo pip3 install selenium
# sudo pip3 install BeautifulSoup4
# you must install chromedriver in your directory

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen
import time


baseUrl = 'https://www.instagram.com/explore/tags'
plusUrl = input('Please write a Tag: ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soupe = BeautifulSoup(html)

inseta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb')as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()
