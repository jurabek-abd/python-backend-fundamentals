from datetime import date, datetime

from data_handler import load_expenses, save_expenses


def find_expense_index(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            return i
    return None


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


def add_expense(args):
    expenses = load_expenses()
    next_id = max((e["id"] for e in expenses), default=0) + 1

    if args.description.strip() == "":
        return {"success": False, "error": "Description can't be empty"}
    if args.category.strip() == "":
        return {"success": False, "error": "Category can't be empty"}
    if args.amount < 0:
        return {"success": False, "error": "Amount can't be below 0"}

    expense = {
        "id": next_id,
        "description": args.description,
        "category": args.category.lower(),
        "amount": args.amount,
        "date": date.today().isoformat(),
    }

    expenses.append(expense)
    save_expenses(expenses)

    return {"success": True, "id": next_id}


def update_expense(args):
    expenses = load_expenses()
    expense_index = find_expense_index(expenses, args.id)

    if expense_index is None:
        return {"success": False, "error": "Expense Not Found. Invalid ID"}

    if args.description is not None and args.description.strip() == "":
        return {"success": False, "error": "Description can't be empty"}
    if args.category is not None and args.category.strip() == "":
        return {"success": False, "error": "Category can't be empty"}
    if args.amount is not None and args.amount < 0:
        return {"success": False, "error": "Amount can't be below 0"}

    expense = expenses[expense_index]

    updates = {
        "description": args.description
        if args.description is not None
        else expense["description"],
        "category": args.category.lower()
        if args.category is not None
        else expense["category"],
        "amount": args.amount if args.amount is not None else expense["amount"],
    }

    for field, value in updates.items():
        if value is not None:
            expense[field] = value

    save_expenses(expenses)
    return {"success": True}


def delete_expense(args):
    expenses = load_expenses()
    expense_index = find_expense_index(expenses, args.id)

    if expense_index is None:
        return {"success": False, "error": "Expense Not Found. Invalid ID"}

    expenses.pop(expense_index)
    save_expenses(expenses)
    return {"success": True}


def list_expenses(args):
    expenses = load_expenses()

    if args.category is not None and args.category.strip() == "":
        return {"success": False, "error": "Category can't be empty"}

    if args.category is not None:
        filtered_expenses = [
            expense for expense in expenses if expense["category"] == args.category
        ]
        return {"success": True, "expenses": filtered_expenses}

    return {"success": True, "expenses": expenses}


def summary_expenses(args):
    expenses = load_expenses()

    if not expenses:
        return {"success": False, "error": "No expenses found."}

    if args.category is not None and args.category.strip() == "":
        return {"success": False, "error": "Category can't be empty"}

    if args.year is not None:
        this_year = datetime.now().year

        if args.year < 1969:
            return {"success": False, "error": "Year can't be below 1969"}
        elif args.year > this_year:
            return {"success": False, "error": f"Year can't be above {this_year}"}
    filtered = (
        e
        for e in expenses
        if (args.month is None or int(e["date"].split("-")[1]) == args.month)
        and (args.category is None or e["category"] == args.category)
        and (args.year is None or int(e["date"].split("-")[0]) == args.year)
    )

    total = round(sum(e["amount"] for e in filtered), 2)

    return {"success": True, "total": total}
