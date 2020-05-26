import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/known_by_Teodor.html"
count = input("Enter times - ")
count = int(count)
pos = input("Enter position - ")
pos = int(pos)

# Ignore SSL certificate errors
for i in range(count):

    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    num = []
    links = []
    tags = soup('a')
    for tag in tags:

        # Look at the parts of a tag
        #print( 'TAG:', tag)
        #print('URL:', tag.get('href', None))
        links.append(tag.get('href', None))
        #print( 'Contents:', tag.contents[0])
        #print( 'Attrs:', tag.attrs)
    print("Retrieving: ", links[pos - 1])
    url = links[pos - 1]



