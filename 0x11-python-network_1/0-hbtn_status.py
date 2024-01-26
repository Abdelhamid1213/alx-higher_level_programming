#!/usr/bin/python3
import urllib.request

"""
This script sends a GET request to https://alx-intranet.hbtn.io/status
and prints the response body, its type, and the UTF-8 decoded content.
"""

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", content.decode('utf-8'))
