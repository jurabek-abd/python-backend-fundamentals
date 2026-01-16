# TMDB CLI Tool

A command-line interface tool to fetch and display movie information from The Movie Database (TMDB) API with Redis caching support.

**Project URL:** https://roadmap.sh/projects/tmdb-cli

## Features

- ✅ Fetch now playing, popular, top-rated, and upcoming movies
- ✅ Redis caching for improved performance (24-hour TTL)
- ✅ Beautiful table formatting with Rich library
- ✅ Pagination support (up to 500 pages)
- ✅ Graceful error handling for API failures
- ✅ Works without Redis (slower, but functional)
- ✅ Command-line argument parsing

## Requirements

- Python 3.10 or higher (uses match/case statements)
- Redis (optional, but recommended for caching)
- TMDB API access token (free)

### Python Dependencies
- requests
- python-dotenv
- redis
- rich

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd tmdb-cli
```

### 2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install requests python-dotenv redis rich
```

### 4. Set up Redis with Docker (Optional but Recommended)
```bash
# Pull and run Redis container
docker run -d --name redis-tmdb -p 6379:6379 --restart unless-stopped redis

# Verify Redis is running
docker ps
```

### 5. Get TMDB API Access Token
1. Sign up at https://www.themoviedb.org/
2. Go to Settings → API
3. Request an API key (free)
4. Copy your "API Read Access Token" (Bearer token)

### 6. Create `.env` file
Create a `.env` file in the project root:
```bash
API_BASE_URL=https://api.themoviedb.org/3
API_ACCESS_TOKEN=your-tmdb-access-token-here
REDIS_HOST=localhost
REDIS_PORT=6379
```

## Project Structure

```
tmdb-cli/
├── api/
│   └── tmdb_client.py         # TMDB API integration
├── cli/
│   └── parser.py              # Command-line argument parsing
├── utils/
│   ├── cache_handler.py       # Redis caching logic
│   └── formatter.py           # Rich table display formatting
├── main.py                    # Application entry point
├── .env                       # Environment variables (create this)
└── README.md
```

## Usage

### Basic Commands

**Get now playing movies:**
```bash
python main.py --type playing
```

**Get popular movies:**
```bash
python main.py --type popular
```

**Get top-rated movies:**
```bash
python main.py --type top
```

**Get upcoming movies:**
```bash
python main.py --type upcoming
```

### Pagination

**Get specific page:**
```bash
python main.py --type popular --page 2
```

**Browse through pages:**
```bash
# Page 1 (default)
python main.py --type top

# Page 5
python main.py --type top --page 5
```

### Example Output

```
# Got cached data

🎬 Movies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Title                Release     Rating  Popularity  Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1   The Godfather        1972-03-14    8.7      12589    The aging patriarch...
2   The Dark Knight      2008-07-16    8.5      11234    Batman raises the...
3   Pulp Fiction         1994-10-14    8.5      10987    A burger-loving...
...
```

## Caching Behavior

- **Cache Duration:** 24 hours (86,400 seconds)
- **Cache Key Format:** `movies:{type}:{page}`
- **Cache Miss:** First request fetches from TMDB and stores in Redis
- **Cache Hit:** Subsequent requests return cached data instantly
- **Cache Failure:** If Redis is unavailable, tool continues to work by fetching fresh data

**Performance Comparison:**
```bash
# First request - fetches from TMDB (~200-500ms)
python main.py --type popular
# Output: # Cache is N/A. Will fetch new data

# Second request - returns from cache (~5-10ms)
python main.py --type popular
# Output: # Got cached data
```

## Available Movie Types

| CLI Type | API Endpoint | Description |
|----------|--------------|-------------|
| `playing` | `now_playing` | Movies currently in theaters |
| `popular` | `popular` | Popular movies by week |
| `top` | `top_rated` | Highest rated movies of all time |
| `upcoming` | `upcoming` | Movies coming soon to theaters |

## Error Handling

The tool handles various error scenarios gracefully:

| Error Type | Message | Description |
|------------|---------|-------------|
| Service Offline (503) | Service temporarily offline | TMDB API is down |
| Internal Error (500) | Something went wrong | Server error on TMDB |
| Rate Limit (429) | Request count over limit | Too many API calls |
| Timeout (504) | Request timed out | Backend server timeout |
| Not Found (404) | Session not found | Invalid endpoint |
| Connection (502) | Couldn't connect | Backend connection failed |

## Development

### Running the Tool

```bash
# Make sure Redis is running (optional)
docker start redis-tmdb

# Run the CLI tool
python main.py --type popular
```

### Code Organization

- **main.py**: CLI entry point and type mapping
- **api/tmdb_client.py**: HTTP requests to TMDB API with error handling
- **cli/parser.py**: Argparse configuration for command-line arguments
- **utils/cache_handler.py**: Redis connection and cache operations
- **utils/formatter.py**: Rich library table formatting for terminal display

### Best Practices Implemented

- ✅ Separation of concerns (API, CLI, caching, formatting)
- ✅ Environment variables for sensitive configuration
- ✅ Type mapping for user-friendly CLI vs API endpoints
- ✅ Graceful degradation when Redis is unavailable
- ✅ Request timeout to prevent hanging
- ✅ Comprehensive error handling
- ✅ Clean terminal output with Rich library

## Troubleshooting

**Redis connection failed:**
- The tool will still work, just slower without caching
- To enable caching, start Redis: `docker start redis-tmdb`
- Check Redis connection: `docker exec -it redis-tmdb redis-cli ping`
- Verify Redis host/port in `.env` file

**API returns errors:**
- Verify `API_ACCESS_TOKEN` is set in `.env`
- Check your TMDB access token is valid at https://www.themoviedb.org/settings/api
- Ensure you're using the "API Read Access Token" (Bearer token), not the API key

**"Data not found" message:**
- Check internet connection
- Verify TMDB API is accessible: https://www.themoviedb.org/
- Review error messages printed above for specific issue
- Try again after a few minutes

**Typo in error messages:**
- Some error messages have "Eror" instead of "Error" (known issue)

**Page validation:**
- Pages are limited to 1-500 by the CLI
- TMDB may not have 500 pages for all movie types
- If you request page 500 but only 50 exist, you'll get an empty results list

## Future Enhancements

Potential improvements for learning:
- Add movie search functionality by title
- Display total pages available from API response
- Add `--cache-bypass` flag to force fresh data
- Implement configurable cache durations per movie type
- Add detailed movie view with cast and crew
- Export results to CSV or JSON
- Add color-coded ratings (green for high, red for low)
- Implement proper logging instead of print statements
- Add unit tests for each component

## Performance Considerations

**With Redis Cache:**
- First request: ~200-500ms (API call + cache store)
- Cached request: ~5-10ms (cache retrieval only)
- Cache hit ratio: High for popular queries

**Without Redis:**
- Every request: ~200-500ms (API call)
- No performance benefit on repeated queries

## Limitations

- Requires Python 3.10+ due to match/case syntax
- Rate limited by TMDB's API limits (check their documentation)
- Pagination numbering assumes 20 movies per page
- Redis connection created per operation (not pooled)
- Error messages printed to stdout instead of stderr

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh TMDB CLI project](https://roadmap.sh/projects/tmdb-cli).

- **The Movie Database (TMDB)**: https://www.themoviedb.org/
- **Redis**: https://redis.io/
- **Rich**: https://github.com/Textualize/rich

---

**Project URL:** https://roadmap.sh/projects/tmdb-cli
