#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
        Converts Roman numeral to an integer

    Args:
        roman_string: A string containing the roman numeral

    Return:
            0 if roman_string is not a string or None
            else: The integer is returned
    '''
    integer = 0
    if roman_string is None or not isinstance(roman_string, str):
        return integer
    rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    while i < len(roman_string):

        if i + 1 < len(roman_string):
            if rom_int[roman_string[i]] < rom_int[roman_string[i+1]]:
                integer +=\
                        rom_int[roman_string[i+1]] - rom_int[roman_string[i]]
                i += 2
                continue
        integer += rom_int[roman_string[i]]
        i += 1
    return integer
