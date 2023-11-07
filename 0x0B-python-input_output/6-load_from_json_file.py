#!/usr/bin/python3
"""Containt a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as f:
        obj = json.load(f)
    return obj
