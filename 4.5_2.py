from bs4 import BeautifulSoup
import requests

# Генерируем ссылки с помощью f-строк
link = []
for i in range(1, 101):
    link.append(f'https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page={i}')
print(link)

# Достаём последний эллемент
url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'

pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

# Тоже что и pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1] только через цикл
result_list = []
for link in soup.find('div', class_='pagen').find_all('a'):
    result_list.append(link.text)
print(pagen)
print(result_list)
