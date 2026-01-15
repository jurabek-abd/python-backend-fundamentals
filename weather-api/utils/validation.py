from datetime import datetime

from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from geopy.geocoders import Nominatim


def is_valid_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_location_string(location_name):
    geolocator = Nominatim(user_agent="weather_api_location_validator")

    try:
        location = geolocator.geocode(location_name)

        if location:
            return True
        return False
    except (GeocoderTimedOut, GeocoderServiceError):
        return False
