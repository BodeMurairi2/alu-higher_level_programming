#!/usr/bin/python3
"""This script fetches contents on the internet
using the request module"""
import requests


if __name__ == "__main___":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    text = response.text
    print("Body response:")
    print("\- type: {}".format(type(text)))
    print("\- content: {}".format(text))
