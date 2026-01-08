import json
import os

FILENAME = "sessions.json"


def load_sessions(filename=FILENAME):
    if not os.path.exists(filename):
        save_sessions([])

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"Warning: {filename} contains invalid JSON. Starting with empty session list."
        )
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}. Starting with empty session list.")
        return []


def save_sessions(sessions=None, filename=FILENAME):
    if sessions is None:
        sessions = []

    try:
        with open(filename, "w") as f:
            json.dump(sessions, f, indent=4)
    except Exception as e:
        print(f"Error saving sessions to {filename}: {e}")
        raise
