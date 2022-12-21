import requests

response = requests.get(url='http://httpbin.org/user-agent')
print(response.text)