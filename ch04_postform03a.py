import requests

url = 'http://www.webscrapingfordatascience.com/postform3/'

# No GET request needed?
# r = requests.get(url)

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