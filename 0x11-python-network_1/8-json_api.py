#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a search query
parameter.

It expects a JSON response and prints the ID and name of the result if found,
or "No result" if no result is found. If the response is not a valid JSON,
it prints "Not a valid JSON".
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <letter as a parameter>')
        quit()

    url = "http://0.0.0.0:5000/search_user"
    data = {
        'q': "" if len(sys.argv) == 1 else sys.argv[1]
    }

    try:
        response = requests.post(url, data).json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
