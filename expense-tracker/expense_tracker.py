import argparse
from expense_manager import add_expense, update_expense, delete_expense, list_expenses, summary_expenses

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--amount", type=int, required=True)
    add_parser.set_defaults(func=add_expense)

    # Update
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description")
    update_parser.add_argument("--category")
    update_parser.add_argument("--amount", type=int)
    update_parser.set_defaults(func=update_expense)

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=delete_expense)

    # List
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument("--category")
    list_parser.set_defaults(func=list_expenses)

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--category")
    summary_parser.add_argument("--month", type=int, choices=range(1, 13))
    summary_parser.set_defaults(func=summary_expenses)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
