#!/usr/bin/python3
"""This module fetches a URL and displays the value of the X-Request-Id
header variable found in the response header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
