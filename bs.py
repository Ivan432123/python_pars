from bs4 import BeautifulSoup
import requests
import lxml

# Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(soup)