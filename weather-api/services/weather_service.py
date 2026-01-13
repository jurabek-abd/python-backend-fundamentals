import os

import requests
from dotenv import load_dotenv
from utils.error_handler import (
    ExternalAPIError,
    InvalidAPIKeyError,
    InvalidLocationError,
    RateLimitError,
    WeatherAPIError,
)

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")
SECRET_KEY = os.getenv("API_SECRET_KEY")


def _build_url_path(location, start_date=None, end_date=None):
    if end_date is not None:
        return f"{BASE_URL}/{location}/{start_date}/{end_date}"
    elif start_date is not None:
        return f"{BASE_URL}/{location}/{start_date}"

    return f"{BASE_URL}/{location}"


def _make_weather_request(url_path):
    payload = {"key": SECRET_KEY}

    r = requests.get(url_path, params=payload)

    return {"status": r.status_code, "data": r.json()}


def get_weather(location, start_date=None, end_date=None):
    url_path = _build_url_path(location, start_date, end_date)
    response = _make_weather_request(url_path)
    status = response["status"]

    if status == 200:
        return response["data"]
    elif status == 404:
        raise InvalidLocationError(f"Location '{location}' not found")
    elif status == 401:
        raise InvalidAPIKeyError("Invalid API key")
    elif status == 429:
        raise RateLimitError("Too many requests, please try again later")
    elif status >= 500:
        raise ExternalAPIError(f"Weather service is down (status: {status})")
    else:
        raise WeatherAPIError(f"Unexpected error: {status}")
