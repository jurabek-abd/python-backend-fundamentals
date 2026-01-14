import json
import os

import redis
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
)


def get_cached_weather(cache_key):
    """Get weather from cache, returns None if not found"""

    cached = r.get(cache_key)

    if cached is None:
        return None

    return json.loads(cached)


def set_cached_weather(cache_key, data, expiration=43200):  # 12 hours default
    """Store weather in cache with expiration"""

    r.set(cache_key, json.dumps(data), ex=expiration)


def get_cache_key(location, start_date=None, end_date=None):
    """Get a unique cache key for this request"""

    if end_date is not None:
        return f"weather:{location}:{start_date}:{end_date}"
    elif start_date is not None:
        return f"weather:{location}:{start_date}"

    return f"weather:{location}"
