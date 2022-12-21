from bs4 import BeautifulSoup

with open('C:/Users/Ivan/PycharmProjects/pars/index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)