import requests
import re
from bs4 import BeautifulSoup
url='https://m.80txt.com/6203/31933511.html'
html=requests.get(url)
web=html.content.decode()
soup=BeautifulSoup(web,'lxml')
#print(soup.title.string)
    #表示读取网页标题
print(soup.prettify())
#print(soup.title)
#print(soup.prettify())
    #prettifl方法表示对网页源码重新补全排版

#print(soup.get_text())
