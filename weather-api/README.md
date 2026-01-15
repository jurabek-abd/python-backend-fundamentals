# Weather API

A RESTful weather API that fetches data from Visual Crossing's API with Redis caching, rate limiting, and comprehensive error handling. Built with Python Flask.

**Project URL:** https://roadmap.sh/projects/weather-api-wrapper-service/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Fetch current weather data for any location
- ✅ Retrieve weather forecasts with date ranges
- ✅ Redis caching for improved performance (12-hour TTL)
- ✅ Graceful degradation when cache is unavailable
- ✅ Rate limiting (5 requests/hour, 20 requests/day) if Redis is down else (10 requests/hour, 50 requests/day)
- ✅ Input validation for locations and dates
- ✅ Comprehensive error handling with custom exceptions
- ✅ Environment variable configuration
- ✅ RESTful API design with JSON responses

## Requirements

- Python 3.10 or higher
- Redis (via Docker or local installation)
- Visual Crossing API key (free tier available)

### Python Dependencies
- Flask 3.1.2 or higher
- redis
- requests
- python-dotenv
- flask-limiter
- geopy

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd python-backend-fundamentals\weather-api
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
pip install Flask redis requests python-dotenv flask-limiter geopy
```

### 4. Set up Redis with Docker
```bash
# Pull and run Redis container
docker run -d --name redis-weather -p 6379:6379 --restart unless-stopped redis

# Verify Redis is running
docker ps
```

### 5. Get Visual Crossing API Key
1. Sign up at https://www.visualcrossing.com/weather-api
2. Get your free API key from the dashboard

### 6. Create `.env` file
Create a `.env` file in the project root:
```bash
API_BASE_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
API_SECRET_KEY=your-visual-crossing-api-key-here
REDIS_HOST=localhost
REDIS_PORT=6379
```

## Project Structure

```
weather-api/
├── routes/
│   └── weather_routes.py      # API endpoint definitions
├── services/
│   ├── cache_service.py       # Redis caching logic
│   └── weather_service.py     # Visual Crossing API integration
├── utils/
│   ├── error_handler.py       # Custom exceptions and error handlers
│   └── validation.py          # Input validation functions
├── app.py                     # Main application entry point
├── config.py                  # Configuration management
├── .env                       # Environment variables (create this)
└── README.md
```

## Usage

### Start the Application

```bash
# Make sure Redis is running
docker start redis-weather

# Start Flask development server
python app.py
```

The API will be available at `http://127.0.0.1:5000`

### API Endpoints

#### Get Current Weather
```bash
GET /weather/<location>
```

**Example:**
```bash
curl http://127.0.0.1:5000/weather/London,UK
```

**Response:**
```json
{
  "status": 200,
  "data": {
    "resolvedAddress": "London, England, United Kingdom",
    "days": [...],
    "currentConditions": {
      "temp": 15.0,
      "conditions": "Partially cloudy",
      "humidity": 75.0
    }
  },
  "message": "Returned fetched data"
}
```

#### Get Weather with Date Range
```bash
GET /weather/<location>?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
```

**Example:**
```bash
curl "http://127.0.0.1:5000/weather/Paris,France?start_date=2026-01-01&end_date=2026-01-07"
```

#### Get Weather for Specific Date
```bash
GET /weather/<location>?start_date=YYYY-MM-DD
```

**Example:**
```bash
curl "http://127.0.0.1:5000/weather/Tokyo,Japan?start_date=2026-01-15"
```

## Caching Behavior

- **Cache Duration:** 12 hours (43,200 seconds)
- **Cache Key Format:** `weather:{location}` or `weather:{location}:{start_date}:{end_date}`
- **Cache Miss:** First request fetches from Visual Crossing and stores in Redis
- **Cache Hit:** Subsequent requests within 12 hours return cached data instantly
- **Cache Failure:** If Redis is unavailable, API continues to work by fetching fresh data

**Example:**
```bash
# First request - fetches from Visual Crossing (200-500ms)
curl http://127.0.0.1:5000/weather/Berlin,Germany

# Second request - returns from cache (2-5ms)
curl http://127.0.0.1:5000/weather/Berlin,Germany
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

| Status Code | Error Type | Description |
|-------------|------------|-------------|
| 200 | Success | Request completed successfully |
| 400 | Bad Request | Invalid date format or malformed request |
| 404 | Not Found | Location not found or doesn't exist |
| 401 | Unauthorized | Invalid API key |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Unexpected error occurred |
| 503 | Service Unavailable | External weather service is down |

**Error Response Format:**
```json
{
  "error": "Location not found: InvalidCity123"
}
```

## Rate Limiting

Protected by flask-limiter to prevent API abuse:

- **5 requests per hour** per IP address
- **20 requests per day** per IP address

**Rate Limit Exceeded Response:**
```json
{
  "error": "Too many requests, please try again later"
}
```

## Input Validation

### Location Validation
- Verifies location exists using Nominatim geocoding service
- Checks for valid location format
- Prevents injection attacks and malformed inputs

### Date Validation
- Format: `YYYY-MM-DD` (e.g., `2026-01-15`)
- Must be valid calendar dates
- Rejects invalid formats like `2026-13-45` or `tomorrow`

## Development

### Running in Debug Mode
```bash
flask --app app --debug run
```

### Testing Cache Behavior
```bash
# Stop Redis to test graceful degradation
docker stop redis-weather

# Make a request - should still work, just slower
curl http://127.0.0.1:5000/weather/London,UK

# Start Redis again
docker start redis-weather
```

### Testing Rate Limiting
```bash
# Make 6 requests within an hour
for i in {1..6}; do curl http://127.0.0.1:5000/weather/London,UK; done
# 6th request should return 429 error
```

### Code Organization

- **app.py**: Flask application setup, middleware, and server configuration
- **config.py**: Centralized environment variable management with validation
- **routes/weather_routes.py**: RESTful endpoint definitions and request handling
- **services/weather_service.py**: External API integration and business logic
- **services/cache_service.py**: Redis operations and cache key management
- **utils/error_handler.py**: Custom exception classes and Flask error handlers
- **utils/validation.py**: Input sanitization and validation logic

### Best Practices Implemented

- ✅ Separation of concerns (routes, services, utilities)
- ✅ Environment variables for sensitive configuration
- ✅ Custom exception hierarchy for specific error handling
- ✅ Centralized error handler registration
- ✅ Graceful degradation when Redis is unavailable
- ✅ Input validation before external API calls
- ✅ Rate limiting to prevent abuse
- ✅ Cache expiration to ensure fresh data
- ✅ RESTful API design with proper HTTP status codes

## Troubleshooting

**Redis connection failed:**
- Verify Redis is running: `docker ps`
- Start Redis: `docker start redis-weather`
- Check Redis connection: `docker exec -it redis-weather redis-cli ping`

**API returns 401 Unauthorized:**
- Verify `API_SECRET_KEY` is set in `.env`
- Check your Visual Crossing API key is valid
- Ensure you haven't exceeded Visual Crossing's rate limits

**Location validation is slow:**
- This is expected - Nominatim geocoding adds 200-500ms per request
- First request is slower, subsequent requests use cache
- Consider removing location validation for better performance

**Rate limit too restrictive:**
- Modify limits in `app.py`:
  ```python
  default_limits=["100 per day", "20 per hour"]
  ```

## Future Enhancements

Potential improvements for learning:
- Add response data transformation (extract only essential fields)
- Implement request logging and analytics
- Add Prometheus metrics for monitoring
- Support multiple cache strategies (current vs forecast vs historical)
- Add API documentation with Swagger/OpenAPI
- Implement async requests for better performance
- Add unit and integration tests
- Support additional weather providers (OpenWeatherMap, WeatherAPI)
- Add webhook support for weather alerts

## Performance Considerations

**With Redis Cache:**
- First request: ~400-700ms (location validation + API call + cache store)
- Cached request: ~5-10ms (location validation + cache retrieval)
- Cache hit ratio: Depends on traffic patterns

**Without Redis:**
- Every request: ~400-700ms (location validation + API call)

**Rate Limits:**
- Visual Crossing free tier: 20 requests/day
- Nominatim: 1 request/second
- Your API: 5 requests/hour per user

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Weather API project](https://roadmap.sh/projects/weather-api-wrapper-service/solutions?u=692db4d2a17ff74763dc81f1).

- **Visual Crossing Weather API**: https://www.visualcrossing.com/weather-api
- **Redis**: https://redis.io/
- **Flask**: https://flask.palletsprojects.com/

---

**Project URL:** https://roadmap.sh/projects/weather-api-wrapper-service/solutions?u=692db4d2a17ff74763dc81f1
