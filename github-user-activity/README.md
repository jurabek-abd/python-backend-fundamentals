# GitHub User Activity CLI

A simple command-line interface (CLI) application to fetch and display GitHub user activity. Built with Python using only standard library modules.

**Project URL:** https://roadmap.sh/projects/github-user-activity/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Fetch recent GitHub activity using the GitHub API
- ✅ Display activity in a clean, readable format
- ✅ Filter events by type (Push, PR, Issues, etc.)
- ✅ Smart caching with expiry to reduce API calls
- ✅ Input validation for GitHub usernames
- ✅ Automatic retry with exponential backoff for rate limits
- ✅ Error handling for network issues and API failures

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jurabek-abd/github-activity-cli.git
cd github-activity-cli
```

2. The project is ready to use! No additional installation required.

## Project Structure

```
github-activity-cli/
├── utils/
│   ├── __init__.py
│   ├── api_client.py          # GitHub API interaction
│   ├── cache_handling.py      # File-based caching
│   └── formatter.py           # Event formatting
├── main.py                     # Entry point
├── cache.json                  # Cache storage (auto-created)
├── .gitignore
└── README.md
```

## Usage

Run the application using Python with the following commands:

### Fetch User Activity

```bash
python main.py <username>
# Output:
# - Pushed to main in octocat/Hello-World
# - Opened pull request #123 in octocat/Spoon-Knife
# - Starred octocat/git-consortium
```

### Filter by Event Type

```bash
# Show only push events
python main.py octocat --type=PushEvent

# Show only pull requests
python main.py octocat --type=PullRequestEvent

# Show only stars
python main.py octocat --type=WatchEvent
```

## Available Event Types

| Event Type | Description |
|------------|-------------|
| `PushEvent` | Code pushes to repositories |
| `PullRequestEvent` | Pull request actions (opened, closed, merged) |
| `IssuesEvent` | Issue actions (opened, closed, reopened) |
| `IssueCommentEvent` | Comments on issues or pull requests |
| `WatchEvent` | Repository stars |
| `ForkEvent` | Repository forks |
| `CreateEvent` | Branch or tag creation |
| `DeleteEvent` | Branch or tag deletion |

## Example Workflow

```bash
# Fetch all activity
python main.py octocat

# Filter by push events
python main.py octocat --type=PushEvent

# Filter by pull requests
python main.py octocat --type=PullRequestEvent

# Filter by stars
python main.py octocat --type=WatchEvent
```

## Error Handling

The application handles various error scenarios gracefully:

- **Invalid usernames**: Validates format before making API requests
- **User not found (404)**: Displays clear error message
- **Rate limits (429)**: Automatically retries with exponential backoff
- **Network issues**: Shows connection error message
- **Server errors (500+)**: Automatically retries failed requests

## Caching

Activity data is cached in `cache.json` to reduce API calls. The cache expires after 10 seconds (configurable in `main.py`).

```bash
# First request - fetches from GitHub API
python main.py octocat

# Second request within 10 seconds - loads from cache
python main.py octocat
# Output: "Loading from cache.json..."
```

## Data Storage

Cache is stored in `cache.json` in the project directory. The file is automatically created on first use.

Example `cache.json` structure:
```json
{
    "octocat": {
        "events": [...],
        "updated_at": "2024-01-05T10:30:00.000000"
    }
}
```

## Development

### Code Organization

- **api_client.py**: Handles GitHub API requests with retry logic
- **cache_handling.py**: Manages JSON cache file operations
- **formatter.py**: Formats different event types for display
- **main.py**: Orchestrates CLI arguments and application flow

### Configuration

Key constants in `main.py`:
- `CACHE_EXPIRY_SECONDS = 10` - Cache duration in seconds
- `MAX_GITHUB_USERNAME_LENGTH = 39` - GitHub's username limit

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh GitHub User Activity project](https://roadmap.sh/projects/github-user-activity/solutions?u=692db4d2a17ff74763dc81f1).

---

**Project URL:** https://roadmap.sh/projects/github-user-activity/solutions?u=692db4d2a17ff74763dc81f1
