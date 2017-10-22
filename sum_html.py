##Uses URLLIB & BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

##Parses requested URL
url = input('Insert URL - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

##Searches for value in tag 'span' ans summarizes it
count = 0
tags = soup('span')
for tag in tags:
	count = count + int(tag.string)

print (count)