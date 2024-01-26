#!/usr/bin/python3
import requests
import sys

"""
This script sends a GET request to a specified URL and retrieves the value
of the 'X-Request-Id' header from the response.
"""

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <URL>')
    quit()

url = sys.argv[1]

with requests.get(url) as response:
    x_request_id = response.headers.get('X-Request-Id', None)

print(x_request_id)
