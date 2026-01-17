import os

from dotenv import load_dotenv

load_dotenv()


BASE_URL = "https://api.github.com/repositories"
DEFAULT_LIMIT = 10
DEFAULT_DURATION = "week"

GITHUB_HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.getenv('GITHUB_PAT')}",
    "X-GitHub-Api-Version": "2022-11-28",
}
