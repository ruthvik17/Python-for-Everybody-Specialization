import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_547196.xml"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print("Data:")
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')

count = []

# while True:
#     c = results[].find('comment').find('count').text
#     print(c)
#     if len(c) < 1:
#         break
#     count.append(int(c))
for i in range(len(results)):
    c = results[i].text
    print(c)
    count.append(int(c))

total = 0
for i in count:
    total = total + i

print("Results:")
print(results)
print("Counts:")
print(count)

print("Total: ", total)