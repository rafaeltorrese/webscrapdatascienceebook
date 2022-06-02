import requests

url = 'http://www.webscrapingfordatascience.com/usercheck/'

r = requests.get(url)
print(r.text)
print(r.request.headers)