#!/usr/bin/python3
""" Program that Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file """
    with open(filename, encoding='utf8') as rf:
        data = json.load(rf)
        return data
