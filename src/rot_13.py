"""Kata: Rot 13 - Text chiper using letter at 13th offset.

#1 Best Practices Solution by warwickwang

import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)

"""

import string


def rot13(message):
    """Return rot13 chiper of imput message."""
    orig = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    chip = "nNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmM"
    try:
        transtab = str.maketrans(orig, chip)
    except AttributeError:
        transtab = string.maketrans(orig, chip)
    return message.translate(transtab)
