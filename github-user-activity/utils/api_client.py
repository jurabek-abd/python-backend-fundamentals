import json
import time
import urllib.error
import urllib.request


def fetch_api_data(url, retries=5, delay=1):
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                data = response.read().decode("utf-8")

                return json.loads(data)
            else:
                print(f"Error: Received status code {response.getcode()}")
                return None
    except urllib.error.HTTPError as e:
        if 500 <= e.code <= 599 and retries > 0:
            time.sleep(delay)
            return fetch_api_data(url, retries - 1, delay * 2)
        elif e.code == 429 and retries > 0:
            time.sleep(delay)
            return fetch_api_data(url, retries - 1, delay * 2)
        elif 400 <= e.code <= 499:
            print(f"( Code: {e.code} ) Error connecting to the API: {e.reason}")
            return None
        raise
    except urllib.error.URLError as e:
        print(f"Error connecting to the API: {e.reason}")
        return None
