import requests

url = 'http://httpbin.org/ip'

with open('proxy_list1.txt') as file:
    proxy_file = iter(file.read().split('\n'))
    for i in range(1, 9217):
        try:
            ip = next(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            print(f'Попытка номер {i}')
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue