#!/usr/bin/python3
"""Containt a function append_write"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
