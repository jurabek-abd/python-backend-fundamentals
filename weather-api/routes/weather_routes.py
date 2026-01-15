from flask import Blueprint, request
from services.cache_service import (
    get_cache_key,
    get_cached_weather,
    set_cached_weather,
)
from services.weather_service import get_weather
from utils.error_handler import InvalidLocationError, WeatherAPIError
from utils.validation import is_valid_date_format, is_valid_location_string

CACHE_EXPIRATION_SECONDS = 43200

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather/<location>")
def get_weather_route(location):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if start_date is not None and not is_valid_date_format(start_date):
        raise WeatherAPIError
    if end_date is not None and not is_valid_date_format(end_date):
        raise WeatherAPIError

    cache_key = get_cache_key(location, start_date, end_date)

    cached_weather = get_cached_weather(cache_key)

    if cached_weather is not None:
        return {
            "data": cached_weather,
        }

    if not is_valid_location_string(location):
        raise InvalidLocationError(location)

    data = get_weather(location, start_date, end_date)

    set_cached_weather(cache_key, data, CACHE_EXPIRATION_SECONDS)
    return {"data": data}
