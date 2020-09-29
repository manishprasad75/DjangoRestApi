# import requests
# import json

# BASE_URL = 'http://127.0.0.1:8000/'
# ENDPOINT = 'api/'

# def get_resources(id = None):
#     data = {}
#     if id is not None:
#         data = {
#             'id': id,
#         }
#     resp = requests.get(BASE_URL+ENDPOINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
# def post_resources():
#     data = {
#         'eno': 400,
#         'ename': "Sumit",
#         'esal': 5000,
#         'eaddr': "Delhi"
#     }
#     resp = requests.post(BASE_URL+ENDPOINT, data=json.dumps(data))
#     print(resp.status_code)
#     data = resp.json()
#     print(data)


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import requests
# import json
# def getTotalGoals(team, year):
#     page = 1
#     payload = {'team1': team, 'year': year, 'page': page}
#     url = "https://jsonmock.hackerrank.com/api/football_matches"
#
#     print(url)
#
#     res = 0
#
#     def getTotalGoals(team, year):
#         page = 1
#         payload = {'team1': team, 'year': str(year), 'page': str(page)}
#         url = "https://jsonmock.hackerrank.com/api/football_matches"
#
#         res = 0
#
#         while (True):
#             payload = {'team1': team, 'year': str(year), 'page': str(page)}
#             resp = requests.get(url, params=payload)
#             data = resp.json()
#             for x in data['data']:
#                 res += int(x.get('team1goals', 0))
#             page += 1
#             if page > int(data['total_pages']):
#                 break
#         page = 1
#         while (True):
#             payload = {'team1': team, 'year': str(year), 'page': str(page)}
#             resp = requests.get(url, params=payload)
#             data = resp.json()
#             for x in data['data']:
#                 res += int(x.get('team2goals', 0))
#             page += 1
#             if page > int(data['total_pages']):
#                 break
#         return res
#
#
# print(getTotalGoals("Barcelona", 2011))


import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def update_resources(id):
    new_data = {
        'id': id,
        'ename': "Manish"
    }
    resp = requests.put(BASE_URL+ENDPOINT, data=json.dumps(new_data))
    print(resp.status_code)
    # if resp.status_code is 200:
    print(resp.json())
    
update_resources('1')
