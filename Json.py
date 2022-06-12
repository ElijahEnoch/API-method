import urllib.request
import json

url = 'http://httpbin.org/get?name=sonic&say=hello'

response = urllib.request.urlopen(url)
response_message = response.read().decode('utf8')

print(response_message)
data = json.loads(response_message)

get_data = data.get('args')

print('name = ', get_data.get('name'))

print('say = ', get_data.get('say'))
