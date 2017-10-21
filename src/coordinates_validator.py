"""Kata: Coordinates Validator - Validate Latitude and Longitude.

#1 Best Practices Solution by daddepledge

def is_valid_coordinates(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180

"""

import re


def is_valid_coordinates(coordinates):
    """Test coordinates for validity."""
    if re.match('^-?\d+\.?\d*\,{1}\s-?\d+\.?\d*$', coordinates):
        lat, lon = coordinates.split(', ')
        return -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180
    else:
        return False
