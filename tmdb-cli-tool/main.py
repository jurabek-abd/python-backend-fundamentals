from api.tmdb_client import get_movies_list
from cli.parser import create_parser
from utils.cache_handler import get_cache_key, get_cached_movies, set_cached_movies
from utils.formatter import display_movies_table

TMDB_MOVIES_LIST_TYPES = {
    "playing": "now_playing",
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming",
}


def main():
    parser = create_parser()
    args = parser.parse_args()

    page = args.page

    if page is None:
        page = 1

    cache_key = get_cache_key(args.type, page)
    cached_data = get_cached_movies(cache_key)

    if cached_data is not None:
        display_movies_table(cached_data, page)
        return

    movie_data = get_movies_list(TMDB_MOVIES_LIST_TYPES[args.type], page)

    if movie_data is None:
        print("\n# Data not found. Try Again")
        return

    set_cached_movies(cache_key, movie_data)

    display_movies_table(movie_data, page)


if __name__ == "__main__":
    main()
