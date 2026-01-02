import json
import urllib.error
import urllib.request


def fetch_api_data(url):
    """
    Fetches data from an API using the standard library
    and returns a Python dictionary/list.
    """

    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                data = response.read().decode("utf-8")

                return json.loads(data)
            else:
                print(f"Error: Received status code {response.getcode()}")
                return None
    except urllib.error.URLError as e:
        print(f"Error connecting to the API: {e.reason}")
        return None
