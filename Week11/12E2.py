import urllib.request
from bs4 import BeautifulSoup
import re

import collections #imported collections and made line 6 because Bsoup was throwing major problems back at me and overflow had this solution
collections.Callable = collections.abc.Callable

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1463132.html').read()
soup = BeautifulSoup(html, "html.parser")

sum=0
# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    span = str(tag)
    #print(span)
    commentnumbers = re.findall("[0-9]+", span)
    for number in commentnumbers :
        number = int(number)
        sum = sum + number
print(sum)
