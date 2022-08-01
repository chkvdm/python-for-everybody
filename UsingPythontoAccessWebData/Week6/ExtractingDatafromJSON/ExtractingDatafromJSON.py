import urllib.request, urllib.parse, urllib.error
import json


counts = list ()

url = input('Enter url: ')
# http://py4e-data.dr-chuck.net/comments_1584020.json

jeyson = urllib.request.urlopen(url).read().decode()
jeyson_dict = json.loads(jeyson)

for user in jeyson_dict["comments"]:
    counts.append(user["count"])

print (len(counts))
print (sum(counts))