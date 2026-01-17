from datetime import date, timedelta


def get_this_day_date():
    """Returns today's date"""
    return f">={date.today()}"


def get_last_7_days_dates(today=None):
    """Returns the date range for the last 7 days (including today)."""
    if today is None:
        today = date.today()
    start_date = today - timedelta(days=6)  # 6 days ago + today = 7 days
    return f"{start_date}..{today}"


def get_last_30_days_dates(today=None):
    """Returns the date range for the last 30 days (including today)."""
    if today is None:
        today = date.today()
    start_date = today - timedelta(days=29)  # 29 days ago + today = 30 days
    return f"{start_date}..{today}"


def get_last_365_days_dates(today=None):
    """Returns the date range for the last 365 days (including today)."""
    if today is None:
        today = date.today()
    start_date = today - timedelta(days=364)  # 364 days ago + today = 365 days
    return f"{start_date}..{today}"
