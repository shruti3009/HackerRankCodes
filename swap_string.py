"""
You are given a string . Your task is to swap cases. In other words, convert all
lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s):
    Swap_string = ""
    for character in s:
        if character.isupper() == True:
            Swap_string = Swap_string + character.lower()
        else:
            Swap_string = Swap_string + character.upper()

    return Swap_string


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
