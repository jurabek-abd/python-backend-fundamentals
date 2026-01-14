from flask import Blueprint, request
from services.cache_service import get_cache_key, get_cached_weather, set_cached_weather
from services.weather_service import get_weather

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather/<location>")
def get_weather_route(location):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    cache_key = get_cache_key(location, start_date, end_date)

    cached_weather = get_cached_weather(cache_key)

    if cached_weather is not None:
        return f"Cached: {cached_weather}"

    data = get_weather(location, start_date, end_date)
    set_cached_weather(cache_key, data, 60)
    return f"Fetched: {data}"
