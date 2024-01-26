#!/usr/bin/python3
import requests
import sys

"""
This script takes a URL as a command-line argument and sends a GET request to
that URL.
If the response status code is not in the 200 range, it prints the error code.
Otherwise, it prints the response text.
"""

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <URL>')
    quit()

try:
    with requests.get(sys.argv[1]) as response:
        response.raise_for_status()
        print(response.text)
except requests.exceptions.HTTPError as e:
    print(f"Error code: {e.response.status_code}")
