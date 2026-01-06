import json
import os

FILENAME = "expenses.json"

def load_expenses(filename=FILENAME):
    if not os.path.exists(filename):
        save_expenses([])
    
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"Warning: {filename} contains invalid JSON. Starting with empty expense list."
        )
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}. Starting with empty expense list.")
        return []

def save_expenses(expenses=None, filename=FILENAME):
    if expenses is None:
        expenses = []

    try:
        with open(filename, "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print(f"Error saving expenses to {filename}: {e}")
        raise