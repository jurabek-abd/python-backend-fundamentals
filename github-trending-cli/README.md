# GitHub Trending CLI

A command-line interface tool to fetch and display trending repositories from GitHub based on recent activity and star count.

**Project URL:** https://roadmap.sh/projects/github-trending-cli/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Fetch trending repositories by time range (day, week, month, year)
- ✅ Configurable result limit (1-100 repositories)
- ✅ Beautiful table formatting with Rich library
- ✅ Sorted by star count (most popular first)
- ✅ No authentication required for basic usage
- ✅ Comprehensive error handling for API failures

## Requirements

- Python 3.7 or higher
- No GitHub authentication required (public API)

### Python Dependencies
- requests
- rich

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd github-trending-cli
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
pip install -r requirements.txt
```

## Project Structure

```
github-trending-cli/
├── api_client.py           # GitHub API integration
├── config.py               # Configuration and constants
├── formatter.py            # Rich table display formatting
├── utils.py                # Date range utility functions
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── README.md
```

## Usage

### Basic Commands

**Get trending repos from the past week (default):**
```bash
python main.py
```

**Get trending repos from today:**
```bash
python main.py --duration day
```

**Get trending repos from the past month:**
```bash
python main.py --duration month
```

**Get trending repos from the past year:**
```bash
python main.py --duration year
```

### Limit Results

**Get top 5 trending repos:**
```bash
python main.py --duration week --limit 5
```

**Get top 50 trending repos:**
```bash
python main.py --duration month --limit 50
```

### Example Output

```
╔═══════════════════════════════════════════════════════════════╗
║            GitHub Repository Search Results                   ║
║            Total repositories found: 1,234                    ║
╚═══════════════════════════════════════════════════════════════╝

                        📚 Repositories                          
╭─────────────────────────────────────────────────────────────────────╮
│ Repository            │ Description          │ ⭐ Stars │ Language  │
├─────────────────────────────────────────────────────────────────────┤
│ user/awesome-project  │ Amazing project...   │ 12,345   │ Python    │
│ dev/cool-tool         │ Useful CLI tool...   │ 8,765    │ Go        │
│ team/web-framework    │ Fast web framework...│ 6,543    │ Rust      │
╰─────────────────────────────────────────────────────────────────────╯

                Showing 10 repositories
```

## Time Range Options

| Duration | Time Range | Description |
|----------|-----------|-------------|
| `day` | Today | Repositories pushed today |
| `week` | Last 7 days | Repositories pushed in the last week |
| `month` | Last 30 days | Repositories pushed in the last month |
| `year` | Last 365 days | Repositories pushed in the last year |

## Error Handling

The tool handles various error scenarios gracefully:

| Error Type | Message | Description |
|------------|---------|-------------|
| Connection Timeout | Failed to fetch repos. Ran out of time | Request took too long |
| Connection Error | Failed to connect to GitHub API | Network issue or GitHub is down |
| Validation Error (422) | Validation failed or endpoint spammed | Invalid query parameters |
| Other Errors | Something went wrong (status XXX) | Unexpected API error |

## Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--duration` | string | `week` | Time range: day, week, month, or year |
| `--limit` | integer | `10` | Number of repos to display (1-100) |

## How It Works

The tool queries GitHub's search API for repositories:
1. Calculates date range based on selected duration
2. Searches for repos pushed within that range
3. Sorts results by total star count (descending)
4. Displays formatted results in a table

**Search Strategy:**
- Uses `pushed:` filter to find recently active repos
- Sorts by total `stars` to show most popular projects
- Combines recent activity with popularity for "trending" effect

## Limitations

- **Limit Range:** Results limited to 1-100 repositories (GitHub API constraint)
- **No Authentication:** Uses public API, subject to rate limits (60 requests/hour per IP)
- **Search Criteria:** Relies on push date + star count, not GitHub's actual trending algorithm
- **API Version:** Locked to GitHub API version 2022-11-28

## Troubleshooting

**Connection timeout:**
- Check your internet connection
- GitHub API might be experiencing high traffic
- Try again after a few moments

**No repositories found:**
- The selected time range might not have enough active repos
- Try a longer duration (e.g., month instead of day)
- GitHub API might be filtering results

**Limit warnings:**
- Limits below 1 are set to default (10)
- Limits above 100 are set to default (10)
- Adjust your `--limit` value to be between 1-100

**Rate limiting:**
- Public GitHub API allows 60 requests/hour without authentication
- If you hit the limit, wait an hour or authenticate with a personal access token
- Consider adding authentication in `config.py` for higher limits (5,000 requests/hour)

## Future Enhancements

Potential improvements for learning:
- Add language filtering (`--language python`)
- Support for topic/tag filtering
- Option to sort by forks or recent activity instead of stars
- Export results to CSV or JSON format
- Add pagination to browse more results
- Implement caching to reduce API calls
- Show repository stats (forks, watchers, issues)
- Add interactive mode to open repos in browser

## Development

### Running the Tool

```bash
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Run with default settings
python main.py

# Run with custom settings
python main.py --duration month --limit 20
```

### Code Organization

- **main.py**: CLI entry point, argument parsing, and orchestration
- **api_client.py**: HTTP requests to GitHub API with error handling
- **config.py**: Configuration constants and date range mapping
- **utils.py**: Date calculation functions for different time ranges
- **formatter.py**: Rich library table formatting for terminal display

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh GitHub Trending CLI project](https://roadmap.sh/projects/github-trending-cli/solutions?u=692db4d2a17ff74763dc81f1).

- **GitHub API**: https://docs.github.com/en/rest
- **Rich**: https://github.com/Textualize/rich

---

**Project URL:** https://roadmap.sh/projects/github-trending-cli/solutions?u=692db4d2a17ff74763dc81f1
