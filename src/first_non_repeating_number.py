"""Kata: First non-repeating number - Return first non-repeating number.

#1 Best Practices Solution by tachyonlabs, gianneng, Echezeaux, john_doe_web

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""

"""


def first_non_repeating_letter(string):
    """Return first non repeating letter or '' if none."""
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    else:
        return ''
