import os

from dotenv import load_dotenv
from utils.error_handler import ExternalAPIError, InvalidAPIKeyError

load_dotenv()

# redis
REDIS_HOST_VAR = "REDIS_HOST"
REDIS_DEFAULT_HOST = "localhost"
REDIS_PORT_VAR = "REDIS_PORT"
REDIS_DEFAULT_PORT = 6379

# weather
BASE_URL_VAR = "API_BASE_URL"

SECRET_KEY_VAR = "API_SECRET_KEY"


def _get_env_variable(name, default):
    value = os.getenv(name)

    if value is None:
        return default
    return value


# redis
def get_redis_host():
    return _get_env_variable(REDIS_HOST_VAR, REDIS_DEFAULT_HOST)


def get_redis_port():
    return int(_get_env_variable(REDIS_PORT_VAR, REDIS_DEFAULT_PORT))


# weather
def get_base_url():
    base_url = _get_env_variable(BASE_URL_VAR, None)

    if base_url is None:
        raise ExternalAPIError

    return base_url


def get_secret_key():
    secret_key = _get_env_variable(SECRET_KEY_VAR, None)

    if secret_key is None:
        raise InvalidAPIKeyError

    return secret_key
