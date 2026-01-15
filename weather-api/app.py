import redis
import redis.exceptions
from config import get_redis_host, get_redis_port
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.weather_routes import weather_bp
from utils.error_handler import register_error_handlers


def is_redis_available():
    try:
        r = redis.Redis(host=get_redis_host(), port=get_redis_port())
        r.ping()
        return True
    except redis.exceptions.RedisError:
        return False


app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(weather_bp)

if is_redis_available():
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["50 per day", "10 per hour"],
        storage_uri="redis://localhost:6379",
    )
else:
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["20 per day", "5 per hour"],
        storage_uri="memory://",
    )

if __name__ == "__main__":
    app.run()
