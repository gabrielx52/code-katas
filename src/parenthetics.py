"""Parnthetics validator."""


def parenthetics(seq):
    """Check if seq has proper parentheses."""
    return_val = 0
    for i in seq:
        if return_val < 0:
            return -1
        if i == '(':
            return_val += 1
        if i == ')':
            return_val -= 1
    if return_val > 0:
        return 1
    return return_val
