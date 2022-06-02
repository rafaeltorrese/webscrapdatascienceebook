import requests


url = 'http://www.webscrapingfordatascience.com/cookielogin/'

# First perform a POST request
r = requests.post(url, data={'username': 'dummy', 'password':'1234'})

# Get the cookie value, either from
# r.header or r.cookies print(r.cookies)
my_cookies = r.cookies

# r.cookies is a RequestsCookieJar object which can also be accesed like a dictionary. The following als works:
my_cookies['PHPSESSID'] = r.cookies.get('PHPSESSID')

# Now perform a GET request to the secret page usign the cookies
page = 'secret.php'
r = requests.get(f'{url}{page}', cookies=my_cookies)

print(r.text)