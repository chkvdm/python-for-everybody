import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
# http://py4e-data.dr-chuck.net/comments_1584017.html

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = list()
tags = soup('span')
for tag in tags:
    count.append(int(tag.contents[0]))

print (len(count))
print (sum(count))