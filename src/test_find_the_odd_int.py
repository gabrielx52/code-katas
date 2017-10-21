"""Test module for find the odd int module."""
import pytest


TEST_CASES = [([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
              ([1, 1, 1, 1, 3], 3),
              ([1, 2, 3, 2, 3], 1),
              ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 62], 62)]


@pytest.mark.parametrize('array, odd_int', TEST_CASES)
def test_find_the_odd_int(array, odd_int):
    """Test for find_it function."""
    from find_the_odd_int import find_it
    assert find_it(array) == odd_int
