import requests


url = 'http://www.webscrapingfordatascience.com/redirlogin/'

# First perform a POST request
r = requests.post(url, data={'username': 'dummy', 'password':'1234'}, allow_redirects=False)

# Get the cookie value, either from r.header or r.cookies 
print(r.cookies)

my_cookies = r.cookies

# Now perform a GET request manually to the  secret page usign the cookies
page = 'secret.php'
r = requests.get(f'{url}{page}', cookies=my_cookies)

print(r.text)