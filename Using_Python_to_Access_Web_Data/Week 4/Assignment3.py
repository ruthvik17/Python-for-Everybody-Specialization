import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
num = []

tags = soup('span')
for tag in tags:
    num.append(int(tag.contents[0]))

total = 0
for i in num:
    total = total + i

print(total)




