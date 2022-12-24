import requests
from bs4 import BeautifulSoup

# Создаём список ссылок на страницы с товарами

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# получаем ссылки из списка тэгов с применением list comprehension:
str = 'https://parsinger.ru/html/'
pagen = [f"{str}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]


# получаем список тэгов (pagen)
def link_list():
    pagen = soup.find('div', class_='pagen').find_all('a')
# print(pagen)

def res():
    res = []
    for i in range(len(pagen)):
        url = pagen[i]
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        b = soup.find_all('a', class_='name_item')
        names = []
        for name in b:
            names.append(name.text)
            res.append(names)
    print(res)


link_list()
res()
