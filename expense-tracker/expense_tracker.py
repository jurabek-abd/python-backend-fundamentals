import argparse

from expense_manager import (
    add_expense,
    delete_expense,
    list_expenses,
    summary_expenses,
    update_expense,
)


def handle_add_expense(args):
    result = add_expense(args)

    if result["success"]:
        print(f"# Expense added successfully (ID: {result['id']})")
    else:
        print(f"# Expense was not added. {result['error']}")


def create_parsers():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # Update
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description")
    update_parser.add_argument("--category")
    update_parser.add_argument("--amount", type=float)

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True)

    # List
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument("--category")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--category")
    summary_parser.add_argument("--month", type=int, choices=range(1, 13))

    return parser.parse_args()


def main():
    args = create_parsers()

    if args.command == "add":
        handle_add_expense(args)
    elif args.command == "delete":
        delete_expense(args)
    elif args.command == "list":
        list_expenses(args)
    elif args.command == "summary":
        summary_expenses(args)
    elif args.command == "update":
        update_expense(args)


if __name__ == "__main__":
    main()
