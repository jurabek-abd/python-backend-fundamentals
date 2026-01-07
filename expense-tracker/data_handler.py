import csv
import json
import os
from datetime import datetime

EXPENSE_STORAGE_FILENAME = "expenses.json"


def export_expenses():
    filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    expenses = load_expenses()

    if not expenses:
        print("# Expenses not exported. No expenses found")
        return

    try:
        with open(filename, mode="w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["id", "description", "category", "amount", "date"]
            )
            writer.writeheader()

            for expense in expenses:
                writer.writerow(
                    {
                        "id": expense["id"],
                        "description": expense["description"],
                        "category": expense["category"],
                        "amount": expense["amount"],
                        "date": expense["date"],
                    }
                )
        print(f"# Expenses exported successfully: {filename}")
    except Exception as e:
        print(f"# Error exporting expenses to a CSV file: {e}")
        raise


def load_expenses(filename=EXPENSE_STORAGE_FILENAME):
    if not os.path.exists(filename):
        save_expenses([])

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"# Warning: {filename} contains invalid JSON. Starting with empty expense list."
        )
        return []
    except Exception as e:
        print(f"# Error reading {filename}: {e}. Starting with empty expense list.")
        return []


def save_expenses(expenses=None, filename=EXPENSE_STORAGE_FILENAME):
    if expenses is None:
        expenses = []

    try:
        with open(filename, "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print(f"# Error saving expenses to {filename}: {e}")
        raise
