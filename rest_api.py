#!usr/bin/env python3

import requests as rq
import json


def read_file():
    """
    read json file and return a dictionary
    """
    request = json.load(open("config.json"))
    return request


if __name__ == "__main__":
    r = read_file()
    if r["method"] == "get":
        response = rq.get(r["url"] + r["endpoint"], params=r["params"])
    print(response.json())
    print(response.status_code)
