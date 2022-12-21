import requests

response = requests.get(url='http://httpbin.org/')
print(type(response))
