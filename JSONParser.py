import urllib.request, urllib.parse, urllib.error
import json

#used examples: http://py4e-data.dr-chuck.net/comments_42.json
#				http://py4e-data.dr-chuck.net/comments_22364.json

url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url)
#reads url and decodes
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)['comments']

print('Count: ', len(info))

sum = 0
for item in info:
	sum = sum + int(item['count'])
print ('Sum: ',sum)