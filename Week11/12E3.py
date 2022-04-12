import urllib.request
from bs4 import BeautifulSoup
import re

import collections #imported collections and made line 6 because Bsoup was throwing major problems back at me and overflow had this solution
collections.Callable = collections.abc.Callable

url = input("Enter URL:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

position = int(input("Enter position:")) - 1 #pos starts at 0
count = int(input("Enter count:"))

for tags in range(count):
    href = soup("a")
    link = href[position].get("href", None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
