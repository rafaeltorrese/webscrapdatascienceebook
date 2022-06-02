import requests

url = 'http://www.webscrapingfordatascience.com/redirect/'

r = requests.get(url)

print(r.text)
print(r.headers)