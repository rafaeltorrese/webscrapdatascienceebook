import requests
base = 'http://www.webscrapingfordatascience.com'

url = f'{base}/authentication/'

r = requests.get(url, auth=('myusername', 'mypassword'))

print(r.text)
print(r.request.headers)