import os

import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")
access_token = os.getenv("API_ACCESS_TOKEN")

headers = {"accept": "application/json", "Authorization": f"Bearer {access_token}"}


def get_movie_list(movies_type, list_page=0):
    url = f"{base_url}/movie/{movies_type}"
    payload = {"language": "en-US", "page": list_page}

    try:
        response = requests.get(url, headers=headers, params=payload)

        match response.status_code:
            case 503:
                raise Exception(
                    "Service offline: This service is temporarily offline, try again later"
                )
            case 500:
                raise Exception("Internal error: Something went wrong, contact TMDB")
            case 429:
                raise Exception(
                    "Your request count (#) is over the allowed limit of (40)"
                )
            case 504:
                raise Exception(
                    "Your request to the backend server timed out. Try again"
                )
            case 404:
                raise Exception("The requested session could not be found")
            case 503:
                raise Exception("The API is undergoing maintenance. Try again later")
            case 502:
                raise Exception("Couldn't connect to the backend server")

        return response.json()
    except Exception as e:
        print(f"\n# Error: {e}")
        return None
