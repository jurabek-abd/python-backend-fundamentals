import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_movies_list(movies_type, list_page=0):
    base_url = os.getenv("API_BASE_URL")
    access_token = os.getenv("API_ACCESS_TOKEN")

    headers = {"accept": "application/json", "Authorization": f"Bearer {access_token}"}

    url = f"{base_url}/movie/{movies_type}"
    payload = {"language": "en-US", "page": list_page}

    response = requests.get(url, headers=headers, params=payload, timeout=30)

    match response.status_code:
        case 200:
            return response.json()
        case 503:
            print(
                "\n# Error: Service offline: This service is temporarily offline, try again later"
            )
        case 500:
            print("\n# Eror: Internal error: Something went wrong, contact TMDB")
        case 429:
            print("\n# Eror: Your request count (#) is over the allowed limit of (40)")
        case 504:
            print("\n# Eror: Your request to the backend server timed out. Try again")
        case 404:
            print("\n# Eror: The requested session could not be found")
        case 502:
            print("\n# Eror: Couldn't connect to the backend server")
        case _:
            print("\n# Eror: Something went wrong. Try again later")

    return None
