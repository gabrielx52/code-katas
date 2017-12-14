"""Test module for Series Sum module."""
import pytest


TEST_CASES = [(1, "1.00"),
              (2, "1.25"),
              (3, "1.39")]


@pytest.mark.parametrize('input, output', TEST_CASES)
def test_series_sum(input, output):
    """Test rot 13 function."""
    from series_sum import series_sum
    assert series_sum(input) == output
