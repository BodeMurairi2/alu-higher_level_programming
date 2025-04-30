#!/usr/bin/python3
"""This module sends a POST request to the URL with the email as
a parameters and display the body of the response decoded in UTF-8
"""
import urllib.request
import urllib.parse
import sys


def send_post_request():
    '''
    This function sends a POST request
    '''
    url = sys.argv[1]
    values = {
        "email": sys.argv[2]
    }
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    with urllib.request.Request(url, data) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    send_post_request()
