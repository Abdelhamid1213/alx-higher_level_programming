#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

"""
This script sends a GET request to a URL provided as a command-line argument
and prints the response body.
If the server returns an HTTP error code, it prints the error code."""

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
