import urllib.request, urllib.parse, urllib.error
import ssl, json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user_address = input ('Enter address: ')
# IUAV Venezia

url = serviceurl + urllib.parse.urlencode({'key' : api_key, 'address' : user_address})
print ('Retrieving url', url)

try:
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    jeyson_dict = json.loads(data)
    place_id = jeyson_dict['results'][0]['place_id']
except:
    jeyson_dict = None
    print ('Error')

print ('Place id: ', place_id)