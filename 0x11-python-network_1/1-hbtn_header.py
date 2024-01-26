#!/usr/bin/python3
import urllib.request
import sys

"""
A script that sends a request to a URL and prints the value of the
'X-Request-Id' header in the response.

Usage: python3 1-hbtn_header.py <URL>
"""

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')

print(x_request_id)
