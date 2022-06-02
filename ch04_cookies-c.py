import requests


url = 'http://www.webscrapingfordatascience.com/trickylogin/'

# First perform a normal GET request to get the form
r = requests.get(url)

# set de cookies already in this point
my_cookies = r.cookies

# Then perform a POST request -- do not follow the redirect
r = requests.post(url, params={'p':'protected'}, data={'username': 'dummy', 'password':'1234'}, allow_redirects=False)

# Now perform a GET request manually to the  secret page usign the cookies
r = requests.get(url, params={'p': 'login'}, cookies=my_cookies)

print(r.text)