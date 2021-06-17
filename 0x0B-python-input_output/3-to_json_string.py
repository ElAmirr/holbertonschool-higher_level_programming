#!/usr/bin/python3
""" Program serialize an object to JSON string """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string) """
    data = json.dumps(my_obj)

    return data
