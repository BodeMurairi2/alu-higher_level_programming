#!/usr/bin/python3
"""This module fetches a URL and displays the value of the X-Request-Id
header variable found in the response header.
"""
import urllib.request
import sys


def fetch_header(url):
    """Fetches a URL and displays the value of the X-Request-Id header."""
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id header
        x_request_id = dict(response.headers).get('X-Request-Id')
        return x_request_id


if __name__ == "__main__":
    print(fetch_header(url))
