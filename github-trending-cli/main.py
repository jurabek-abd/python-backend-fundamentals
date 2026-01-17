import argparse

from api_client import get_public_repos
from config import DEFAULT_DURATION, DEFAULT_LIMIT
from formatter import format_repos


def create_parser():
    parser = argparse.ArgumentParser(description="GitHub Trending CLI")

    parser.add_argument(
        "--duration",
        type=str,
        choices=["day", "week", "month", "year"],
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

    if limit < 1:
        limit = DEFAULT_LIMIT

        print("\n# Limit can't be below 1. It will be set to 10 to avoid crashing")
        return
    elif limit > 100:
        limit = DEFAULT_LIMIT

        print("\n# Limit can't be aboce 100. It will be set to 10 to avoid crashing")
        return

    repos = get_public_repos(args.duration, args.limit)

    if repos is None:
        print("\n# Could not fetch repos. Try again")
        return
    elif len(repos) == 0:
        print("\n No repos found")
        return

    format_repos(repos)


if __name__ == "__main__":
    main()
