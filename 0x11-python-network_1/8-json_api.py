#!/usr/bin/python3
import requests
import sys

"""
This script sends a POST request to a specified URL with a search query
parameter.

It expects a JSON response and prints the ID and name of the result if found,
or "No result" if no result is found. If the response is not a valid JSON,
it prints "Not a valid JSON".
"""

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <letter as a parameter>')
    quit()

url = "http://0.0.0.0:5000/search_user"
data = {
    'q': (sys.argv[1] if len(sys.argv) == 2 else "")
}

with requests.post(url, data) as response:
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
