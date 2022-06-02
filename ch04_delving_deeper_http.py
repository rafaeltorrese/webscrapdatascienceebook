import requests

url = 'http://www.webscrapingfordatascience.com/postform2/'

r = requests.get(url)

formdata = {
    'name': 'Juan Perez',
    'gender': 'M',
    'pizza': 'like',
    'salad': 'like',
    'haircolor':  'brown',
    'comments': 'No comments',
}

r = requests.post(url, data=formdata)
print(r.text)