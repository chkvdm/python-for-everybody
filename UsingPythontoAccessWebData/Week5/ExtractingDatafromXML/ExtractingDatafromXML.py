import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
# http://py4e-data.dr-chuck.net/comments_1584019.xml

xml_doc = urllib.request.urlopen(url, context=ctx).read()
comment = ET.fromstring(xml_doc)
counts = comment.findall('.//count')

comment_sum = 0
for item in counts:
    comment_sum += int(item.text)

print (len(counts))
print (comment_sum)