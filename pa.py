import requests
from bs4 import BeautifulSoup
url='https://m.80txt.com/6203/31933511.html'
html=requests.get(url)
web=html.content.decode()
xs=BeautifulSoup(web,'lxml')
print(xs.get_text())
