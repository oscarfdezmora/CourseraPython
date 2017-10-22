##Uses URLLIB & BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

##Parses requested URL
url = input('Insert URL - ')
count = int(input('Insert count - '))
position = int(input('Insert position - '))
print ('Retrieving - ',url)
index1 = 1

while (index1 <= count):
	
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')

	index2 = 1
	tags = soup('a')
	for tag in tags:
		if (index2==position):
			url = tag.get('href', None)
			print ('Retrieving - ',url)
			break
		index2 = index2 +1

	index1 = index1 +1