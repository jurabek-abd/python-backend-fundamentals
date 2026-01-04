import argparse
import re
import sys
from datetime import datetime

from utils.api_client import fetch_api_data
from utils.cache_handling import load_cache, save_cache
from utils.formatter import format_activity

CACHE_EXPIRY_SECONDS = 10


def create_parser():
    parser = argparse.ArgumentParser(description="GitHub User Activity CLI")

    parser.add_argument("username", type=str, help="GitHub Account Username")
    parser.add_argument(
        "--type",
        type=str,
        choices=[
            "PushEvent",
            "IssueCommentEvent",
            "PullRequestEvent",
            "CreateEvent",
            "DeleteEvent",
            "IssuesEvent",
            "WatchEvent",
            "ForkEvent",
        ],
        help="GitHub Feed Event Type",
    )

    return parser


def is_valid_github_username(username):
    pattern = r"^[A-Za-z0-9-]*$"

    if not username:
        return False

    if username.startswith("-") or username.endswith("-"):
        return False

    regex_match = re.match(pattern, username)

    length_ok = len(username) < 40

    if regex_match and length_ok:
        return True

    return False


def is_cache_fresh(cache, username, cache_expiry_seconds=CACHE_EXPIRY_SECONDS):
    if cache.get(username):
        time_difference = datetime.now() - datetime.fromisoformat(
            cache[username]["updated_at"]
        )

        if time_difference.total_seconds() >= cache_expiry_seconds:
            return False
        return True
    return False


def output_activity(events, event_type):
    if event_type is not None:
        filtered_events = [event for event in events if event["type"] == event_type]
        format_activity(filtered_events)
        return

    format_activity(events)


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not is_valid_github_username(args.username):
        print("\nPlease enter valid GitHub username!")
        sys.exit(1)

    cache = load_cache()

    if is_cache_fresh(cache, args.username):
        print("\nLoading from cache.json...")
        output_activity(cache[args.username]["events"], args.type)
        return

    url = f"https://api.github.com/users/{args.username}/events"

    events = fetch_api_data(url)

    if events is None:
        sys.exit(1)

    cache[args.username] = {}
    cache[args.username]["events"] = events
    cache[args.username]["updated_at"] = datetime.now().isoformat()
    save_cache(cache)
    output_activity(events, args.type)


if __name__ == "__main__":
    main()
