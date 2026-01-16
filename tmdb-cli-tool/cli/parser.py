import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool")

    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["playing", "popular", "top", "upcoming"],
        help="Movie List Type",
    )
    parser.add_argument(
        "--page", type=int, choices=range(1, 501), help="Movie List Page"
    )

    return parser
