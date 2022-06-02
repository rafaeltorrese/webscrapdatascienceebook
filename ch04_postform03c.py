import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/postform3/'

# First performed a Get request
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html')
p_val = soup.find('input', attrs={'name': 'protection'}).get('value')


# includes 'protection' field. See tag in html
formdata = {
    'name': 'Juan Perez',
    'gender': 'M',
    'pizza': 'like',
    'salad': 'like',
    'haircolor':  'brown',
    'comments': 'No comments',
    'protection': p_val,
}

r = requests.post(url, data=formdata)
print(r.text)