#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""

    new_line_chars = ['.', '?', ':']

    for char in text:
        formatted_text += char

        if char in new_line_chars:
            formatted_text += '\n\n'

    lines = formatted_text.split('\n')

    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            print(line.strip())
        else:
            print(line.strip(), end='')
