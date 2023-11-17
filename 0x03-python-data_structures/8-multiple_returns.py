#!/usr/bin/python3
def multiple_returns(sentence):
    """
        Creates a tuple containing the length of a string, and its
        first character

        Args:
            setence: The sentence

        Returns:
            The newly generated tuple
    """
    length = len(sentence)
    if length == 0:
        return (0, None)
    else:
        return (length, sentence[0])
