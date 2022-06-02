# %%
import requests
from  requests import  Session
#%%
url = 'http://www.webscrapingfordatascience.com/trickylogin/'
my_session = Session()
my_session.headers.update({'User-Agent': 'Chrome!'})

# All requests in this session will now use this User-Agent header:

r = my_session.post(url)
print(r.request.headers)

r = my_session.post(url, params={'p': 'login'}, data={'username': 'dummy', 'password':'1234'})
print(r.request.headers)

r = my_session.get(url, params={'p': 'protected'})
print(r.text)