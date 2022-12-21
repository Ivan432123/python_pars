import requests
import time

url = 'http://httpbin.org/'
response = requests.get(url)


def status(url, response):
    print(response.status_code)

    if response.status_code == 200:
        print("status_code OK")
    else:
        print("status_code NOT OK")

    if response.status_code != 200:
        time.sleep(60)
    else:
        print("status_code OK... Continue execute code...")


status(url, response)
