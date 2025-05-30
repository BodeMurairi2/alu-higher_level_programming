#!/usr/bin/python3
"""This module defines a function that fetches the status of a URL."""
import urllib.request


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
