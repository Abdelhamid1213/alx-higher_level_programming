#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

"""This script sends a POST request to a specified URL with an email parameter.

Usage: python3 2-post_email.py <URL> <email>
"""

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} <URL> <email>')
    quit()

url = sys.argv[1]
data = {
    'email': sys.argv[2]
}

encoded_data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data=encoded_data, method='POST')


with urllib.request.urlopen(request) as response:
    result = response.read()
    print(result.decode('utf-8'))
