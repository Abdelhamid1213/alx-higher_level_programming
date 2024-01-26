#!/usr/bin/python3
import requests
import sys

"""
This script sends a POST request to a specified URL with an email parameter.
The URL and email are provided as command-line arguments.
"""

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} <URL> <email>')
    quit()

url = sys.argv[1]
data = {
    'email': sys.argv[2]
}

with requests.post(url, data) as response:
    print(response.text)
