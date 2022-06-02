import requests

url = 'http://www.webscrapingfordatascience.com/postform3/'

# No GET request needed?
# r = requests.get(url)

# includes 'protection' field. See tag in html
formdata = {
    'name': 'Juan Perez',
    'gender': 'M',
    'pizza': 'like',
    'salad': 'like',
    'haircolor':  'brown',
    'comments': 'No comments',
    'protection': '7ed2c7e6bdb947b6c79818f06853623c',
}

r = requests.post(url, data=formdata)
print(r.text)