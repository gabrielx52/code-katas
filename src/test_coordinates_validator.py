"""Test module for Coordinates Validator module."""
import pytest


valid_coordinates = [
    "-23, 25",
    "4, -3",
    "24.53525235, 23.45235",
    "04, -23.234235",
    "43.91343345, 143",
    "0, -0",
    "-90, -180"
]


invalid_coordinates = [
    "23.234, - 23.4234",
    "2342.43536, 34.324236",
    "N23.43345, E32.6457",
    "99.234, 12.324",
    "6.325624, 43.34345.345",
    "0, 1,2",
    "0.342q0832, 1.2324",
    "23.245, 1e1",
    "--389,9.9",
    "90.0,, 181"
]


@pytest.mark.parametrize("coords", valid_coordinates)
def test_is_valid_coordinates_true(coords):
    """Testing the lucas function from series module."""
    from coordinates_validator import is_valid_coordinates
    assert is_valid_coordinates(coords)


@pytest.mark.parametrize("coords", invalid_coordinates)
def test_is_valid_coordinates_false(coords):
    """Testing the lucas function from series module."""
    from coordinates_validator import is_valid_coordinates
    assert not is_valid_coordinates(coords)
