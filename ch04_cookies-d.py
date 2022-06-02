import requests


url = 'http://www.webscrapingfordatascience.com/trickylogin/'

# First perform a normal GET request to get the form
r = requests.get(url)

# set de cookies
my_cookies = r.cookies
print(my_cookies)

# Then perform a POST request -- do not follow the redirect. Use te cookies we got before
r = requests.post(url, params={'p':'protected'}, data={'username': 'dummy', 'password':'1234'}, allow_redirects=False, cookies=my_cookies)

# We need to update our cookies again. Note that the PHPSESSID value will have changed
my_cookies = r.cookies
print(my_cookies)

# Now perform a GET request manually to the  secret page usign the cookies using updated cookies
r = requests.get(url, params={'p': 'login'}, cookies=my_cookies)

print(r.text)