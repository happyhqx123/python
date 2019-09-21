import requests 
from bs4 import BeautifulSoup
url=requests.get('https://www.baidu.com')
print (url.content.decode())
