# GitHub User Activity CLI

A command-line interface tool to fetch and display recent GitHub activity for any user. Built with Python using only standard library modules.

> **Status**: 🚧 Work in Progress

This project is part of the [roadmap.sh Backend Projects](https://roadmap.sh/projects/github-user-activity) series.

## Features

- Fetch recent GitHub activity using the GitHub API
- Display activity in a clean, readable format
- Filter events by type (Push, Issue Comments, Pull Requests)
- Built using only Python standard library (no external dependencies)

## Requirements

- Python 3.6 or higher
- Internet connection (to access GitHub API)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd github-user-activity
```

2. No additional dependencies needed! This project uses only Python's standard library.

## Usage

### Basic Usage

Fetch and display all recent activity for a GitHub user:

```bash
python main.py <username>
```

**Example:**
```bash
python main.py yyx990803
```

**Output:**
```
Output:

- Pushed to rebrand in vitejs/vite
- Commented on issue #9345 in vitest-dev/vitest
- Opened pull request #736 in oxc-project/oxc-project.github.io
- Pushed to main in rolldown/rolldown
```

### Filter by Event Type

Filter activity to show only specific event types:

```bash
python main.py <username> --type <event_type>
```

**Available event types:**
- `PushEvent` - Code pushes
- `IssueCommentEvent` - Comments on issues or pull requests
- `PullRequestEvent` - Pull request actions (opened, closed, merged)

**Examples:**
```bash
# Show only push events
python main.py yyx990803 --type PushEvent

# Show only pull request events
python main.py yyx990803 --type PullRequestEvent

# Show only issue comments
python main.py yyx990803 --type IssueCommentEvent
```

## Project Structure

```
github-user-activity/
│
├── main.py                  # Entry point and CLI argument handling
├── utils/
│   ├── api_client.py       # GitHub API interaction
│   └── formatter.py        # Event formatting and display
└── README.md               # Project documentation
```

## How It Works

1. **API Client** (`api_client.py`): 
   - Makes HTTP requests to GitHub's public API
   - Handles network errors gracefully
   - Returns parsed JSON data

2. **Formatter** (`formatter.py`):
   - Processes event data
   - Formats different event types appropriately
   - Displays clean, readable output

3. **Main** (`main.py`):
   - Parses command-line arguments
   - Coordinates API calls and formatting
   - Handles event filtering

## Error Handling

The application handles common errors:
- **Invalid username**: Displays appropriate error message
- **Network failures**: Catches and reports connection errors
- **API rate limits**: Shows HTTP status code errors
- **Invalid event types**: Argument parser prevents invalid filter types

## Learning Objectives

This project helps practice:
- Working with REST APIs
- Handling JSON data in Python
- Building command-line interfaces with `argparse`
- Error handling and defensive programming
- Code organization and modularity
- Using Python's standard library (`urllib`, `json`, `argparse`)

## Roadmap / To-Do

- [✅] Add more event types (WatchEvent, ForkEvent, CreateEvent, etc.)
- [✅] Implement caching to reduce API calls
- [✅] Handle GitHub API rate limiting more gracefully
- [ ] Improve Code Quality

## GitHub API Information

This project uses the GitHub Events API:
- **Endpoint**: `https://api.github.com/users/<username>/events`
- **Documentation**: [GitHub Events API](https://docs.github.com/en/rest/activity/events)
- **Rate Limit**: 60 requests per hour for unauthenticated requests

## Limitations

- Currently displays only the most recent events (GitHub API returns up to 30 events)
- No authentication implemented (subject to lower rate limits)
- Only three event types are formatted (more can be added)

## Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Submit a pull request with improvements
- Share feedback on code structure and practices

## License

This project is open source and available for educational purposes.

## Acknowledgments

- Project idea from [roadmap.sh](https://roadmap.sh/projects/github-user-activity)
- GitHub API documentation and community

---

**Project Status**: This is a work-in-progress learning project. Features and functionality are being actively developed.
