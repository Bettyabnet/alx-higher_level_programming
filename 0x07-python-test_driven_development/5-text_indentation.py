#!/usr/bin/python3
""" Defining  a function that prints a text"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = [".", "?", ":"]
    start_index = 0
    end_index = 0

    while end_index < len(text):
        if text[end_index] in punctuation_chars:
            print(text[start_index:end_index + 1].strip())
            print()
            start_index = end_index + 1

        end_index += 1

    if start_index < len(text):
        print(text[start_index:].strip())
