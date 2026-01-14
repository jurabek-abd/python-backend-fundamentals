from flask import Blueprint, request
from services.weather_service import get_weather

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather/<location>")
def get_weather_route(location):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    data = get_weather(location, start_date, end_date)
    return f"{data}"
