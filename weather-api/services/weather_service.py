import requests
from config import get_base_url, get_secret_key
from dotenv import load_dotenv
from utils.error_handler import (
    ExternalAPIError,
    InvalidAPIKeyError,
    InvalidLocationError,
    RateLimitError,
    WeatherAPIError,
)

load_dotenv()

BASE_URL = get_base_url()
SECRET_KEY = get_secret_key()


def _build_url_path(location, start_date=None, end_date=None):
    if end_date is not None:
        return f"{BASE_URL}/{location}/{start_date}/{end_date}"
    elif start_date is not None:
        return f"{BASE_URL}/{location}/{start_date}"

    return f"{BASE_URL}/{location}"


def _make_weather_request(url_path):
    payload = {"key": SECRET_KEY}

    r = requests.get(url_path, params=payload)

    match r.status_code:
        case 200:
            return r.json()
        case 404:
            raise InvalidLocationError("Location not found")
        case 401:
            raise InvalidAPIKeyError("Invalid API key")
        case 429:
            raise RateLimitError("Too many requests, please try again later")
        case 500:
            raise ExternalAPIError(f"Weather service is down (status: {r.status_code})")
        case _:
            raise WeatherAPIError(f"Unexpected error: {r.status_code}")


def get_weather(location, start_date=None, end_date=None):
    url_path = _build_url_path(location, start_date, end_date)
    response = _make_weather_request(url_path)

    return response
