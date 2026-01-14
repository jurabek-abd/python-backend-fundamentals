from flask import Flask
from routes.weather_routes import weather_bp
from utils.error_handler import register_error_handlers

app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(weather_bp)
