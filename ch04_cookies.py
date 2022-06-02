import requests


url = 'http://www.webscrapingfordatascience.com/cookielogin/secret.php'

my_cookies = {'PHPSESSID':'co6ufb3t25mfv4ohgu20v7h3mm'}
r = requests.get(url, cookies=my_cookies)


print(r.text)