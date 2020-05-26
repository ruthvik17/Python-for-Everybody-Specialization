import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_547197.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print("Data:")
print(data.decode())

info = json.loads(data)
print('User count:', len(info))


count = []

for item,value in info.items():
    if item == "comments":
        for i in info[item]:
            count.append(int(i['count']))
total = 0

for i in count:
    total = total + i

print("Total: ", total)


print(count)