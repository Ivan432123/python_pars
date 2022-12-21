from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)

r_e = response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')


def price_wath(url, response, r_e, soup):
     div = soup.find_all('p', class_='price')
     x = 0
     for price in div:
         p=price.text
         p=p.replace(" руб", " ")
         x+=int(p)
         print(x)

def price():
    url = 'https://parsinger.ru/html/hdd/4/4_1.html'
    response = requests.get(url=url)
    r_e = response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find('div', 'sale', 'span')
    print(div)

    x = 0
    for txt in div:
        price = txt.text
        price = price.replace(" руб", " ")
        p=int(price)

       # print(p)

#price_wath(url, response, r_e, soup)
price()


