"""Kata: Find the odd int - Find the int that is in the sequence odd amt times.

#1 Best Practices Solution by cerealdinner, ynnake, sfr, netpsychosis,
                              VadimPopov, user7514902 (plus 291 more warriors)

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

"""


def find_it(seq):
    """Return the int that is in seq odd amount of times."""
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
