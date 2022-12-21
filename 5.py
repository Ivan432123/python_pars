from fake_useragent import UserAgent
import requests
import time
url = 'http://httpbin.org/user-agent'

for x in range(100):
    ua = UserAgent()
    time.sleep(1)
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)