class WeatherAPIError(Exception):
    """Base exception for all weather API errors"""

    def __init__(self, message="An error occured"):
        self.message = message

    def __str__(self):
        return self.message

    pass


class InvalidLocationError(WeatherAPIError):
    """Raised when a location cannot be found"""

    def __init__(self, location, message="Location not found"):
        self.location = location
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.location}"


class InvalidAPIKeyError(WeatherAPIError):
    """Raised when the API key is invalid or missing (401)"""

    pass


class RateLimitError(WeatherAPIError):
    """Raised when API rate limit is exceeded (429)"""

    pass


class ExternalAPIError(WeatherAPIError):
    """Raised when the external weather service has problems (5xx)"""

    pass


def register_error_handlers(app):
    """Register error handlers with the Flask app"""

    @app.errorhandler(InvalidLocationError)
    def handle_invalid_location(e):
        return {"error": str(e)}, 404

    @app.errorhandler(InvalidAPIKeyError)
    def handle_invalid_api_key(e):
        return {"error": "Invalid API key"}, 401

    @app.errorhandler(RateLimitError)
    def handle_rate_limit(e):
        return {"error": str(e)}, 429

    @app.errorhandler(ExternalAPIError)
    def handle_external_api_error(e):
        return {"error": "Weather service temporarily unavailable"}, 503

    @app.errorhandler(WeatherAPIError)
    def handle_general_weather_error(e):
        return {"error": str(e)}, 500
