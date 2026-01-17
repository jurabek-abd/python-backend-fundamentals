from utils import (
    get_last_7_days_dates,
    get_last_30_days_dates,
    get_last_365_days_dates,
    get_this_day_date,
)

BASE_URL = "https://api.github.com/search/repositories"
DEFAULT_LIMIT = 10
MAX_LIMIT = 100
MIN_LIMIT = 1
DEFAULT_DURATION = "week"
DURATION_OPTIONS = ["day", "week", "month", "year"]

GITHUB_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

GITHUB_TIMEOUT_SECONDS = 30

DATE_RANGES = {
    "day": get_this_day_date,
    "week": get_last_7_days_dates,
    "month": get_last_30_days_dates,
    "year": get_last_365_days_dates,
}
