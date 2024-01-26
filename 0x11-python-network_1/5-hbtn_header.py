#!/usr/bin/python3
import requests
import sys

""" """

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <URL>')
    quit()

url = sys.argv[1]

with requests.get(url) as response:
    x_request_id = response.headers['X-Request-Id']

print(x_request_id)
