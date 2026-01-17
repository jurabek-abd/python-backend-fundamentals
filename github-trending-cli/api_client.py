import requests
from config import BASE_URL, GITHUB_HEADERS, GITHUB_TIMEOUT_SECONDS


def fetch_repos(date_range, limit=10):
    params = {
        "q": f"pushed:{date_range}",
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }

    try:
        response = requests.get(
            BASE_URL,
            headers=GITHUB_HEADERS,
            params=params,
            timeout=GITHUB_TIMEOUT_SECONDS,
        )

        return response.status_code, response.json()
    except requests.exceptions.ConnectTimeout:
        print("\n# Failed to fetch github repos. Ran out of time. Try Again")
    except requests.exceptions.ConnectionError:
        print(
            "\n# Failed to connect to the GitHub API. Chech your network connection and try again"
        )
