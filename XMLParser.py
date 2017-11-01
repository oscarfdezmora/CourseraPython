import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

lst = tree.findall('.//count')
print('Count: ', len(lst))

sum = 0
for item in lst:
	sum = sum +int(item.text)
print ('Sum: ',sum)

#    results = tree.findall('result')
#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text

#    print('lat', lat, 'lng', lng)
#    print(location)
