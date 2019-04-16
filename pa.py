import requests
from bs4 import BeautifulSoup
url='https://m.80txt.com/6203/31933511.html'
html=requests.get(url)
web=html.content.decode()
xs=BeautifulSoup(web,'lxml')
zw=re.search(r'刘峰看着(.*?)没有留下。',xs.get_text())
print(zw)

