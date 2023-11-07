#!/usr/bin/python3
"""Containt a function class_to_json"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
