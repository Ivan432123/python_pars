import requests
from bs4 import BeautifulSoup
def get_html(url):
    resp = requests.get(url=url)
    resp.encoding = 'utf-8'
    return resp.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def main():
    url = 'http://parsinger.ru/html/index3_page_1.html'
    soup = get_data(get_html(url))
    pages = soup.find('div', class_='pagen').findAll('a')
    page = int(pages[-1].text)
    s = []
    for i in range(1, page + 1):
        url_1 = f'http://parsinger.ru/html/index3_page_{i}.html'
        soup_1 = get_data(get_html(url_1))
        items = [item.text for item in soup_1.select('.name_item')]
        s.append(items)
    print(s)

if __name__ == '__main__':
    main()