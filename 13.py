from bs4 import BeautifulSoup
import requests
import time

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
r_e = response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

url_2 = 'http://parsinger.ru/html/headphones/5/5_32.html'
response_2 = requests.get(url=url_2)
r_e_2 = response_2.encoding = 'utf-8'
soup_2 = BeautifulSoup(response_2.text, 'lxml')


# Поиск по class class='item'
def class_item(url, response, r_e, soup):
    div = soup.find('div', 'item')
    # print(div)
    for txt in div:
        print(txt.text)
    print("                                        СПАРСИЛИ ITEM                                 ")


# Получаем все теги <li>
def teg_li(url, response, r_e, soup):
    div = soup.find('div', 'item').find_all('li')
    # print(div)
    for txt in div:
        print(txt.text)
    print("                                       ПОЛУЧИЛИ ВСЕ ТЕГИ <li>                ")


# Парсим артикул
def class_article(url_2, response_2, r_e_2, soup_2):
    div = soup_2.find('p', class_='article').text
    print(div)
    print("                                       Спарсили артикул                  ")


# Парсим по ID
def pars_id(url_2, response_2, r_e_2, soup_2):
    div = soup_2.find('p', id='p_header').text
    print(div)
    print("                                 СПАРСИЛИ по ID            ")

# Парсим по атрибутам
def pars_atribute(url_2, response_2, r_e_2, soup_2):
    div = soup_2.find('span', {'name':'count'}).text
    print(div)
    print("                        СПАРСИЛИ АТРИБУТ name='count' ИЗ ТЭГА 'span'  ")

class_item(url, response, r_e, soup)
time.sleep(3)
teg_li(url, response, r_e, soup)
time.sleep(3)
class_article(url_2, response_2, r_e_2, soup_2)
time.sleep(3)
pars_id(url_2, response_2, r_e_2, soup_2)
time.sleep(3)
pars_atribute(url_2, response_2, r_e_2, soup_2)
