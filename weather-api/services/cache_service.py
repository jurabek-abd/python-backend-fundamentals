import json

import redis
import redis.exceptions
from config import get_redis_host, get_redis_port

DEFAULT_CACHE_EXPIRATION_SECONDS = 43200

r = redis.Redis(
    host=get_redis_host(),
    port=get_redis_port(),
    decode_responses=True,
)


def get_cached_weather(cache_key):
    """Get weather from cache, return None if not found"""

    try:
        cached = r.get(cache_key)

        if cached is None:
            return None

        return json.loads(cached)
    except redis.exceptions.ConnectionError:
        return None


def set_cached_weather(
    cache_key, data, expiration=DEFAULT_CACHE_EXPIRATION_SECONDS
):  # 12 hours default
    """Store weather in cache with expiration"""

    try:
        r.set(cache_key, json.dumps(data), ex=expiration)
    except redis.exceptions.ConnectionError:
        return None


def get_cache_key(location, start_date=None, end_date=None):
    """Get a unique cache key for this request"""

    if end_date is not None:
        return f"weather:{location}:{start_date}:{end_date}"
    elif start_date is not None:
        return f"weather:{location}:{start_date}"

    return f"weather:{location}"
