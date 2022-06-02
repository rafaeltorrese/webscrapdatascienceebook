import requests


url = 'http://www.webscrapingfordatascience.com/trickylogin/'

# First perform a POST request -- do not follow the redirect
# Note that the ?p=login parameter needs to be set
r = requests.post(url, params={'p':'login'}, data={'username': 'dummy', 'password':'1234'}, allow_redirects=False)

# set de cookies
my_cookies = r.cookies

# Now perform a GET request manually to the  secret page usign the cookies
r = requests.get(url, params={'p': 'login'}, cookies=my_cookies)

print(r.text)