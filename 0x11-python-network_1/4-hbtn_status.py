#!/usr/bin/python3
import requests

"""
This script sends a GET request to https://alx-intranet.hbtn.io/status
and prints the response body, type, and content.
"""

url = "https://alx-intranet.hbtn.io/status"

with requests.get(url) as response:
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
