from api.tmdb_client import get_movie_list
from cli.parser import create_parser
from utils.cache_handler import get_cache_key, get_cached_movies, set_cached_movies
from utils.formatter import print_movies


def main():
    parser = create_parser()
    args = parser.parse_args()

    page = args.page

    if page is None:
        page = 1

    if page < 1:
        print("\n# Page can't be below 1. The tool will set it to 1 to avoid crashing")
        page = 1

    cache_key = get_cache_key(args.type, page)
    cached_data = get_cached_movies(cache_key)

    if cached_data is not None:
        print_movies(cached_data, page)
        return

    data = None

    match args.type:
        case "playing":
            data = get_movie_list("now_playing", page)
        case "popular":
            data = get_movie_list("popular", page)
        case "top":
            data = get_movie_list("top_rated", page)
        case "upcoming":
            data = get_movie_list("upcoming", page)

    if data is None:
        print("\n# Data is None. Try Again")
        return

    set_cached_movies(cache_key, data, 45)

    print_movies(data, page)


if __name__ == "__main__":
    main()
