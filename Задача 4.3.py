import requests, zipfile, time
from bs4 import BeautifulSoup

url = "https://parsinger.ru/downloads/cooking_soup/index.zip"


# Загружает файл в указанную папку
def download_file(url):
    response = requests.get(url=url, stream=True)
    with open('C:/Users/Ivan/PycharmProjects/pars/index.zip', 'wb') as file:
        file.write(response.content)
        print("download zip ok")
        time.sleep(5)


# Распаковывает файл из скачанного zip-архива в указанную дирректорию
def unzip_file():
    archive = 'index.zip'
    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extractall('C:/Users/Ivan/PycharmProjects/pars')
        print("unzip_file status: OK")
        time.sleep(5)


# Извлекает из index.html его содержимое при помощи bs4 и парсера 'lxml'
def data_extraction():
    with open('C:/Users/Ivan/PycharmProjects/pars/index.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        print(soup)


download_file(url)
unzip_file()
data_extraction()
