"""Kata: Sum of the first nth term of Series - Find nth item of series.

#1 Best Practices Solution by MMMAAANNN, doctornick5, Slx64, ninja37,
                         FablehavenGeek, nabrarpour4 (plus 17 more warriors)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""
from __future__ import division


def series_sum(n):
    """Return nth item of sum series."""
    total = 0
    denom = 1
    for i in range(n):
        total += 1 / denom
        denom += 3
    return '{:.2f}'.format(total)
