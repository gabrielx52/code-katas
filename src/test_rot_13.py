"""Test module for Rot 13 module."""
import pytest


TEST_CASES = [("test", "grfg"),
              ("Test", "Grfg"),
              ('Gabriel', 'Tnoevry'),
              ('Meringolo', 'Zrevatbyb'),
              ('python', 'clguba'),
              ('potato', 'cbgngb')]


@pytest.mark.parametrize('input, output', TEST_CASES)
def test_rot13(input, output):
    """Test rot 13 function."""
    from rot_13 import rot13
    assert rot13(input) == output
