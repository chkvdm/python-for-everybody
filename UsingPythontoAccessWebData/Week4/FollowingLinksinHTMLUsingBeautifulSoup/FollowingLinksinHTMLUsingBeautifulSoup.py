import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = int(input('count '))
pstn = int(input('position '))

for turn in range(count):
    link = list()
    name = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lnk = tag.get('href', None)
        link.append(lnk)
        nm = tag.contents[0]
        name.append(nm)
    print (name[pstn-1])
    url = link[pstn-1]
    continue