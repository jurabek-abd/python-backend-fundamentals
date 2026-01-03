import argparse
from datetime import datetime

from utils.api_client import fetch_api_data
from utils.cache_handling import load_cache, save_cache
from utils.formatter import format_activity

CACHE_EXPIRY = 10


def output_activity(events, event_type):
    if event_type is not None:
        filtered_events = [event for event in events if event["type"] == event_type]
        format_activity(filtered_events)
        return

    format_activity(events)


def main():
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

    args = parser.parse_args()

    cache = load_cache()

    cached_user = cache.get(args.username)

    if cached_user is not None:
        time_difference = datetime.now() - datetime.fromisoformat(
            cached_user["updated_at"]
        )

        if time_difference.total_seconds() >= CACHE_EXPIRY:
            cache.pop(args.username)
            save_cache(cache)
        else:
            print("\nLoading from cache.json...")
            output_activity(cached_user["events"], args.type)
            return

    url = f"https://api.github.com/users/{args.username}/events"

    events = fetch_api_data(url)

    if events is None:
        return

    cache[args.username] = {}
    cache[args.username]["events"] = events
    cache[args.username]["updated_at"] = datetime.now().isoformat()
    save_cache(cache)
    output_activity(events, args.type)


if __name__ == "__main__":
    main()
