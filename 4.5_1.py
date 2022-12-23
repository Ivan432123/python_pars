import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')


# Получаем список тегов страниц .find_all('a'):
def tag_list():
    pagen = soup.find('div', class_='pagen').find_all('a')
    print(pagen)


# Применим list comprehension, чтобы извлечь ссылку и текст:
def list_comprehension():
    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    print(pagen)


# То же самое что list comprehension, только через цикл:
def list_for():
    pagen = soup.find('div', class_='pagen').find_all('a')
    list_link = []
    for link in pagen:
        list_link.append(link['href'])

    print(list_link)


# Генерируем корректные ссылки
# Создадим переменную shema и сохраним в нее первую часть ссылки. И в цикле на каждой итерации мы будем склеивать обе части, чтобы получить корректную ссылку.
def shema():
    pagen = soup.find('div', class_='pagen').find_all('a')

    list_link = []
    shema = 'http://parsinger.ru/html/'
    for link in pagen:
        list_link.append(f"{shema}{link['href']}")

    print(list_link)


# То же самое, но с применением list comprehension:
def shema_list_comprehension():
    shema = 'http://parsinger.ru/html/'
    pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
    print(pagen)


shema_list_comprehension()
