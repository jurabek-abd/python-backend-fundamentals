import argparse

from data_handler import export_expenses
from expense_manager import (
    add_expense,
    delete_expense,
    list_expenses,
    summary_expenses,
    update_expense,
)


def print_expenses(expenses):
    if not expenses:
        print("# Expenses not listed. No expenses found")
        return

    headers = ["ID", "Date", "Description", "Category", "Amount"]

    rows = [
        [str(e["id"]), e["date"], e["description"], e["category"], f"${e['amount']}"]
        for e in expenses
    ]

    # Calculate column widths
    col_widths = [
        max(len(header), max(len(row[i]) for row in rows))
        for i, header in enumerate(headers)
    ]

    # Print header
    header_line = "  ".join(
        header.ljust(col_widths[i]) for i, header in enumerate(headers)
    )
    print(header_line)
    print("-" * len(header_line))

    # Print rows
    for row in rows:
        print("  ".join(row[i].ljust(col_widths[i]) for i in range(len(row))))


def handle_add_expense(args):
    result = add_expense(args)

    if result["success"]:
        print(f"# Expense added successfully (ID: {result['id']})")
    else:
        print(f"# Expense not added. {result['error']}")


def handle_delete_expense(args):
    result = delete_expense(args)

    if result["success"]:
        print(f"# Expense deleted successfully (ID: {args.id})")
    else:
        print(f"# Expense not deleted. {result['error']}")


def handle_list_expenses(args):
    result = list_expenses(args)

    if result["success"]:
        print_expenses(result["expenses"])
    else:
        print(f"# Expenses not listed. {result['error']}")


def handle_summary_expenses(args):
    result = summary_expenses(args)

    if not result["success"]:
        print(f"# Expenses not summarized. {result['error']}")
        return

    if args.year is not None and args.month is not None:
        print(
            f"# Total expenses for {args.category or 'all'} in {args.month}/{args.year}: ${result['total']}"
        )
    elif args.month is not None:
        # only month
        print(f"# Total expenses for month {args.month}: ${result['total']}")
    elif args.year is not None:
        # only year
        print(f"# Total expenses for year {args.year}: ${result['total']}")
    elif args.category:
        print(f"# Total expenses for {args.category}: ${result['total']}")
    else:
        print(f"# Total expenses: ${result['total']}")


def handle_update_expense(args):
    result = update_expense(args)

    if result["success"]:
        print(f"# Expense updated successfully (ID: {args.id})")
    else:
        print(f"# Expense not updated. {result['error']}")


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
    summary_parser.add_argument("--year", type=int)

    # Export
    subparsers.add_parser("export", help="Export to a CSV file")

    return parser.parse_args()


def main():
    args = create_parsers()

    if args.command == "add":
        handle_add_expense(args)
    elif args.command == "delete":
        handle_delete_expense(args)
    elif args.command == "list":
        handle_list_expenses(args)
    elif args.command == "summary":
        handle_summary_expenses(args)
    elif args.command == "update":
        handle_update_expense(args)
    elif args.command == "export":
        export_expenses()


if __name__ == "__main__":
    main()
