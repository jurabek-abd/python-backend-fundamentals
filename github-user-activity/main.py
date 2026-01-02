import argparse

from utils.api_client import fetch_api_data
from utils.formatter import format_activity


def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity CLI")

    parser.add_argument("username", type=str, help="GitHub Account Username")
    parser.add_argument(
        "--type",
        type=str,
        choices=["PushEvent", "IssueCommentEvent", "PullRequestEvent"],
        help="GitHub Feed Event Type",
    )

    args = parser.parse_args()

    url = f"https://api.github.com/users/{args.username}/events"

    events = fetch_api_data(url)

    if events is None:
        return

    if args.type is not None:
        filtered_events = [event for event in events if event["type"] == args.type]
        format_activity(filtered_events)
        return

    format_activity(events)


if __name__ == "__main__":
    main()
