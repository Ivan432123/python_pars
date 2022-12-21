from bs4 import BeautifulSoup
import requests


def price():
    url = 'http://parsinger.ru/html/hdd/4/4_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    old_price = int(soup.find('span', id='old_price').text.replace(' руб', ''))
    price = int(soup.find('span', id='price').text.replace(' руб', ''))
    res = (old_price - price) * 100 / old_price
    print(round(res, 1))


price()
