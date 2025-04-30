#!/usr/bin/python3
"""This module defines a function that fetches the status of a URL."""
import urllib.request


def fetch_status(url='https://alu-intranet.hbtn.io/status'):
    """Fetches the status of a URL and prints the response."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response: ")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
        print("\t- status code: {}".format(response.getcode()))
        print("\t- headers: {}".format(response.getheaders()))
        print("\t- URL: {}".format(response.geturl()))
        print("\t- status:".format(response.status))


if __name__ == "__main__":
    fetch_status()
