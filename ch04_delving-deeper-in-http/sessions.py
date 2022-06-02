# %%
import requests
from  requests import  Session
#%%
url = 'http://www.webscrapingfordatascience.com/trickylogin/'
my_session = Session()

r = my_session.post(url)
r = my_session.post(url, params={'p': 'login'}, data={'username': 'dummy', 'password':'1234'})

r = my_session.get(url, params={'p': 'protected'})
print(r.text)