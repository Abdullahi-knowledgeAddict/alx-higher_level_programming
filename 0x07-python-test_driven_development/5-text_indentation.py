#!/usr/bin/python3

"""A simple module containing simple function that appends two newlines to the
    ". , ? and :"
"""


def text_indentation(text):
    """Appends 2 new lines for every '.' , ',', '?', and ':'
    encountered while printing text

    Args:
        text: The variable that holds the string to be printed

   """

    if type(text) != str:
        raise TypeError('text must be a string')

    # Now printing
    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print('\n')  # printing Double newline
