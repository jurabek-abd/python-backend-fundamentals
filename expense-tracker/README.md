# Expense Tracker CLI

A simple command-line interface (CLI) application to track and manage your personal expenses. Built with Python using only standard library modules.

**Project URL:** https://roadmap.sh/projects/expense-tracker/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Add new expenses with description, category, and amount
- ✅ Update existing expenses
- ✅ Delete expenses by ID
- ✅ List all expenses with formatted output
- ✅ Filter expenses by category
- ✅ View expense summaries with flexible filters
- ✅ Filter summaries by month, year, and category
- ✅ Export expenses to CSV with timestamps
- ✅ Input validation and error handling
- ✅ Support for decimal amounts
- ✅ Persistent storage using JSON

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jurabek-abd/expense-tracker.git
cd expense-tracker
```

2. The project is ready to use! No additional installation required.

## Project Structure

```
expense-tracker/
├── data_handler.py         # JSON file operations and CSV export
├── expense_manager.py      # Expense management logic
├── expense_tracker.py      # Entry point and CLI interface
├── expenses.json           # Expense storage (auto-created)
├── .gitignore
└── README.md
```

## Usage

Run the application using Python with the following commands:

### Adding an Expense

```bash
python expense_tracker.py add --description "Lunch" --category "Food" --amount 20
# Output: Expense added successfully (ID: 1)

python expense_tracker.py add --description "Netflix" --category "Entertainment" --amount 15.99
# Output: Expense added successfully (ID: 2)
```

### Updating an Expense

```bash
# Update description
python expense_tracker.py update --id 1 --description "Lunch with friends"
# Output: Expense updated successfully (ID: 1)

# Update amount
python expense_tracker.py update --id 1 --amount 25.50
# Output: Expense updated successfully (ID: 1)

# Update multiple fields
python expense_tracker.py update --id 1 --description "Dinner" --category "Food" --amount 30
# Output: Expense updated successfully (ID: 1)
```

### Deleting an Expense

```bash
python expense_tracker.py delete --id 2
# Output: Expense deleted successfully (ID: 2)
```

### Listing Expenses

```bash
# List all expenses
python expense_tracker.py list

# List expenses by category
python expense_tracker.py list --category "Food"
```

### Viewing Summaries

```bash
# View total expenses
python expense_tracker.py summary
# Output: Total expenses: $150.50

# View expenses for a specific month
python expense_tracker.py summary --month 1
# Output: Total expenses for month 1: $75.25

# View expenses for a specific year
python expense_tracker.py summary --year 2026
# Output: Total expenses for year 2026: $150.50

# View expenses for a specific category
python expense_tracker.py summary --category "Food"
# Output: Total expenses for Food: $45.50

# Combine filters
python expense_tracker.py summary --month 1 --category "Food"
# Output: Total expenses for Food in 1/2026: $20.00
```

### Exporting to CSV

```bash
python expense_tracker.py export
# Output: Expenses exported successfully: expenses_20260107_143022.csv
```

## Expense Properties

Each expense contains the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | Integer | Unique identifier (auto-incremented) |
| `description` | String | Expense description |
| `category` | String | Expense category (e.g., Food, Transport, Entertainment) |
| `amount` | Float | Expense amount (supports decimals) |
| `date` | String | ISO 8601 date when expense was created |

## Example Workflow

```bash
# Add some expenses
python expense_tracker.py add --description "Grocery shopping" --category "Food" --amount 85.50
python expense_tracker.py add --description "Bus" --category "Transport" --amount 2.50
python expense_tracker.py add --description "Movie tickets" --category "Entertainment" --amount 24.00
python expense_tracker.py add --description "Coffee" --category "Food" --amount 4.50

# List all expenses
python expense_tracker.py list

# View total spending
python expense_tracker.py summary

# Check food expenses
python expense_tracker.py summary --category "Food"

# Update an expense
python expense_tracker.py update --id 1 --description "Grocery shopping at a shop" --amount 92.75

# Delete an expense
python expense_tracker.py delete --id 3

# Export to CSV for record keeping
python expense_tracker.py export
```

## Error Handling

The application handles various error scenarios gracefully:

- **Empty descriptions/categories**: Validates that fields are not empty or whitespace-only
- **Negative amounts**: Prevents adding expenses with amounts below 0
- **Non-existent expenses**: Displays clear error messages when trying to update or delete expenses that don't exist
- **Invalid year ranges**: Validates year is between 1969 and current year
- **Corrupted JSON**: Automatically recovers from corrupted storage files by starting with an empty expense list
- **File operations**: Handles file read/write errors with informative messages

## Data Storage

Expenses are stored in `expenses.json` in the project directory. The file is automatically created on first use.

Example `expenses.json` structure:
```json
[
    {
        "id": 1,
        "description": "Lunch",
        "category": "Food",
        "amount": 20.0,
        "date": "2026-01-07"
    },
    {
        "id": 2,
        "description": "Bus",
        "category": "Transport",
        "amount": 2.5,
        "date": "2026-01-07"
    }
]
```

## Development

### Code Organization

- **data_handler.py**: Manages JSON file operations and CSV export functionality
- **expense_manager.py**: Contains all expense manipulation logic with validation and return-value pattern
- **expense_tracker.py**: Handles command-line argument parsing and output formatting

### Best Practices Implemented

- ✅ Separation of concerns across modules
- ✅ Return values instead of printing from business logic
- ✅ Input validation and error handling
- ✅ Clear success/error messages for better UX
- ✅ Dynamic column width formatting for clean output
- ✅ Support for decimal amounts using float type
- ✅ Flexible filtering and summary options

### Running Tests

To test the application manually:

1. Test adding expenses with various amounts (integers and decimals)
2. Test updating expenses with partial updates
3. Test deleting expenses
4. Test listing with and without category filters
5. Test summaries with various filter combinations
6. Test export functionality
7. Test error cases (empty strings, negative amounts, non-existent IDs)
8. Verify JSON file structure in `expenses.json`

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Expense Tracker project](https://roadmap.sh/projects/expense-tracker/solutions?u=692db4d2a17ff74763dc81f1).

---

**Project URL:** https://roadmap.sh/projects/expense-tracker/solutions?u=692db4d2a17ff74763dc81f1
