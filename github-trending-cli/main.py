import argparse

from api_client import fetch_repos
from config import (
    DATE_RANGES,
    DEFAULT_DURATION,
    DEFAULT_LIMIT,
    DURATION_OPTIONS,
    MAX_LIMIT,
    MIN_LIMIT,
)
from formatter import output_repos


def create_parser():
    parser = argparse.ArgumentParser(description="GitHub Trending CLI")

    parser.add_argument(
        "--duration",
        type=str,
        choices=DURATION_OPTIONS,
        default=DEFAULT_DURATION,
        help="Specifies the time i.e. `day`, `week`, `month`, `year`). Default to `week`.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="Specifies the number of repositories to display. Default to `10`.",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    limit = args.limit

    if limit < MIN_LIMIT:
        limit = DEFAULT_LIMIT

        print(
            f"\n# Limit can't be below {MIN_LIMIT}. It will be set to {DEFAULT_LIMIT} to avoid crashing"
        )
    elif limit > MAX_LIMIT:
        limit = DEFAULT_LIMIT

        print(
            f"\n# Limit can't be above {MAX_LIMIT}. It will be set to {DEFAULT_LIMIT} to avoid crashing"
        )

    status, response = fetch_repos(DATE_RANGES[args.duration](), limit)

    if not status == 200:
        print(f"\n# {response['message']}")
        print("\n# See all the errors below:\n")

        for error in response.get("errors"):
            print(f"# {error['message']}")

        return

    if response is None:
        return
    elif len(response.get("items")) == 0:
        print("\n# No repos found")
        return

    output_repos(response)


if __name__ == "__main__":
    main()
