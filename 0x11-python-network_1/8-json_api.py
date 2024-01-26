#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a letter as parameter.
It then receives a JSON response and prints the ID and name from the response.
If the response is empty, it prints "No result".
If the response is not a valid JSON, it prints "Not a valid JSON".
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
