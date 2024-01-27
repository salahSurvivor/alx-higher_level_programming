#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib

This script sends a GET request to the specified URL and prints
information about the response body, its type, content, and utf-8 content.
"""

import urllib.request

def fetch_status(url):

    with urllib.request.urlopen(url) as response:
        return response.read()

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    body = fetch_status(url)

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
