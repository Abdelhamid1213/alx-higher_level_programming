#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

"""
A script that retrieves the user ID from the GitHub API using basic
authentication.

This script takes two command-line arguments: the GitHub username and password.
It sends a GET request to the GitHub API with the provided credentials and
retrieves the user information.

The user ID is then extracted from the response and printed to the console.
"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    token = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=token)
    print(request.json().get('id'))
