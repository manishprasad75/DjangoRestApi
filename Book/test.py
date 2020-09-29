# import requests 
# BASE_URL = 'http://0.0.0.0:8080/'
# ENDPOINT = 'api/'

# # 0.0.0.0:8080/api

# resp = requests.get(BASE_URL+ENDPOINT)
# print(resp.status_code)
# print(resp.json())
# print(resp)

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.youtube.com')
for line in fhand:
    print(line.decode().strip())