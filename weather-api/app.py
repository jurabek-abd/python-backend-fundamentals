from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.weather_routes import weather_bp
from utils.error_handler import register_error_handlers

app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(weather_bp)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per day", "5 per hour"],
    storage_uri="redis://localhost:6379",
)
