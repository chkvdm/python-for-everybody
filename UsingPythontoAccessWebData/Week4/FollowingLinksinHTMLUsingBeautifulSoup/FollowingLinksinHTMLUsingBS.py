import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = int(input('count '))
pstn = int(input('position '))
name = list()



# Version_1. Iteration.

for turn in range(count):
    link = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pstn-1].get('href', None)
    name.append(tags[pstn - 1].contents[0])
    continue

print ('\n'.join(name))



# version_2. Recurcion.

def find_name(url, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pstn - 1].get('href', None)
    nm = tags[pstn - 1].contents[0]
    name.append(nm)
    if count > 1:
        find_name(url, (count) - 1)

find_name(url, count)
print ('\n'.join(name))