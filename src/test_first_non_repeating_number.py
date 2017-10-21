"""Test module for first non repeating number module."""

import pytest

TEST_CASES = [('a', 'a'),
              ('stress', 't'),
              ('moonmen', 'e'),
              ('', ''),
              ('abba', ''),
              ('aa', ''),
              ('~><#~><', '#'),
              ('hello world, eh?', 'w'),
              ('sTreSS', 'T'),
              ('Go hang a salami, I\'m a lasagna hog!', ','),
              ('This is really cool', 'T'),
              ('moooooo', 'm'),
              ('1999', '1'),
              ('beeb', '')]


@pytest.mark.parametrize('input, output', TEST_CASES)
def test_first_non_repeating_number(input, output):
    """Test for first non repeating number function."""
    from first_non_repeating_number import first_non_repeating_letter
    assert first_non_repeating_letter(input) == output
