# import json
#
# import requests
#
# BASE_URL = 'http://127.0.0.1:8000/'
# ENDPOINT = 'api/'
#
#
# def get_resource(id):
#     resp = requests.get(BASE_URL + ENDPOINT + id + '/')
#     print(resp.status_code)
#     print(resp.json())
#
#
# def get_all():
#     resp = requests.get(BASE_URL + ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#
#
# def create_resource():
#     new_emp = dict(eno=800, ename='Shashank', esal=10000.0, eaddr='Chennai')
#     resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
#
# def update_resource(id):
#     new_emp = dict(ename='Vickey', esal=12000, eaddr='Delhi')
#     resp = requests.put(BASE_URL+ENDPOINT+id+'/', data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# def delete_resource(id):
#     new_emp = dict(ename='Vickey', esal=12000, eaddr='Delhi')
#     resp = requests.delete(BASE_URL+ENDPOINT+id+'/', data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
#
# delete_resource('8')


import requests

url = "https://myallies-breaking-news-v1.p.rapidapi.com/news/cnn"

headers = {
    'x-rapidapi-host': "myallies-breaking-news-v1.p.rapidapi.com",
    'x-rapidapi-key': "31131ffb1amsh3fae29b29e908ffp1ec293jsnb7a0f5c8f606"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)