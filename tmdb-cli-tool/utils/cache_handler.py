import json
import os

import redis
import redis.exceptions
from dotenv import load_dotenv

load_dotenv()

DEFAULT_CACHE_EXPIRATION_SECONDS = 86400  # 24 hours


r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
)


def get_cached_movies(cache_key):
    """Get movies from cache, return None if not found"""

    try:
        if cached is None:
            print("\n# Cache is N/A. Will fetch new data")
            return None

        print("\n# Got cached data")
        return json.loads(cached)
    except redis.exceptions.ConnectionError:
        print("\n# Failed to get cached movies. Redis is down")
        return None


def set_cached_movies(cache_key, data, expiration=DEFAULT_CACHE_EXPIRATION_SECONDS):
    """Store movies in cache with expiration"""

    try:
        r.set(cache_key, json.dumps(data), ex=expiration)
        print("\n# Movies cached")
    except redis.exceptions.ConnectionError:
        print("\n# Failed to cache movies. Redis is down")
        return None


def get_cache_key(movies_type, list_page=1):
    """Get a unique cache key for this request"""

    return f"movies:{movies_type}:{list_page}"
