#!/bin/bash
# This script is used to retrieve the body of a response from a given URL.
# It sends a GET request to the URL and prints the body of the response.

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$response" -eq 200 ]; then
    curl -s "$1"
else
    echo "Error: Response status code is not 200"
fi
