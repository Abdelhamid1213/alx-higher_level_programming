#!/usr/bin/python3
"""Containt a function read_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, "a", encoding='utf-8') as f:
        f.write(text)
    return len(text)
