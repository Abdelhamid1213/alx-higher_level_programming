#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response.
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

size=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n')

if [ -n "$size" ]; then
    echo "$size"
else
    echo "Unable to determine the size of the response body"
fi
