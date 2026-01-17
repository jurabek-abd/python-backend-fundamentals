import requests
from config import BASE_URL, GITHUB_HEADERS


def get_public_repos(duration="week", limit=10):
    response = requests.get(BASE_URL, headers=GITHUB_HEADERS)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 304:
        print(f"\n# Error: Not modified (status {response.status_code})")
    elif response.status_code == 422:
        print(
            f"\n# Error: Validation failed, or the endpoint has been spammed (status {response.status_code})"
        )
    else:
        print(f"\n Error: Something went wrong (status {response.status_code}")

    return None
