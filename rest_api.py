#!/usr/bin/env python3

import requests
import json


def read_file():
    """
    Read json file and return a dictionary
    """
    request = json.load(open("config.json"))
    return request


def request_get(get_url, params):
    """
    Send a GET request
    """
    return requests.get(get_url, params=params)


def request_post(post_url, data):
    """
    Send a POST request
    """
    return requests.post(post_url, data=data)


def main():
    methods = {
        "post": request_post,
        "get": request_get
    }
    r = read_file()
    response = methods[r["method"]](r["url"] + r["endpoint"], r["payload"])
    result = response.json()
    if result["ok"]:
        print(result)
    else:
        print(result["error"])


if __name__ == "__main__":
    main()
