from datetime import date
from data_handler import load_expenses, save_expenses

def find_expense_index(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            return i
    return None

def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    headers = ["ID", "Date", "Description", "Category", "Amount"]

    rows = [
        [
            str(e["id"]),
            e["date"],
            e["description"],
            e["category"],
            f"${e['amount']}"
        ]
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
        print(
            "  ".join(
                row[i].ljust(col_widths[i]) for i in range(len(row))
            )
        )


def add_expense(args):
    expenses = load_expenses()
    next_id = max((e["id"] for e in expenses), default=0) + 1
    
    expense = {
        "id": next_id,
        "description": args.description,
        "category": args.category.lower(),
        "amount": args.amount,
        "date": date.today().isoformat()
    }
    
    expenses.append(expense)
    save_expenses(expenses)

def update_expense(args):
    expenses = load_expenses()
    expense_index = find_expense_index(expenses, args.id)
    
    if expense_index is None:
        print("Expense Not Found. Invalid ID")
        return
    
    expense = expenses[expense_index]
    
    updates = {
        "description": args.description,
        "category": args.category.lower(),
        "amount": args.amount,
    }
    
    for field, value in updates.items():
        if value is not None:
            expense[field] = value
    
    save_expenses(expenses)

def delete_expense(args):
    expenses = load_expenses()
    expense_index = find_expense_index(expenses, args.id)
    
    if expense_index is None:
        print("Expense Not Found. Invalid ID")
        return
    
    expenses.pop(expense_index)
    save_expenses(expenses)

def list_expenses(args):
    expenses = load_expenses()
    
    if args.category is not None:
        filtered_expenses = [expense for expense in expenses if expense["category"].lower() == args.category.lower()]
        print_expenses(filtered_expenses)
        return
    
    print_expenses(expenses)

def summary_expenses(args):
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    filtered = (
        e for e in expenses
        if (args.month is None or int(e["date"].split("-")[1]) == args.month)
        and (args.category is None or e["category"].lower() == args.category.lower())
    )
    
    total = sum(e["amount"] for e in filtered)
    
    if args.month and args.category:
        print(f"Total expenses for {args.category} in month {args.month}: ${total}")
    elif args.month:
        print(f"Total expenses for month {args.month}: ${total}")
    elif args.category:
        print(f"Total expenses for {args.category}: ${total}")
    else:
        print(f"Total expenses: ${total}")
    
    