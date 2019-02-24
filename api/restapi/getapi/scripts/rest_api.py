#!/usr/bin/env python3

import requests
import json


def pair_keyvalue(key_list, value_list):
    paired_dict = {}

    for key, value in zip(key_list, value_list):
        if key:
            paired_dict[key] = value
    return paired_dict


def get_response(url, method, params={}, data={}, headers={}, json={}):
    methods = {
        "get": requests.get,
        "post": requests.post,
        "put": requests.put,
        "delete": requests.delete,
        "head": requests.head,
        "options": requests.options
    }
    response = methods[method](url,
                               params=params,
                               data=data,
                               headers=headers,
                               json=json
                               )
    save_file(response.text)
    return response.text


def save_file(result):
    with open("result", "w+") as f:
        f.write(result)
        print("Done")
