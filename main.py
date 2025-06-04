import sys
import json
from datetime import datetime

#JSON
JSON_FILE = "expense.json"

#load json
def load_expense():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# generate new ID
def new_id(tasks):
    if not tasks:
        return 1
    return max(t['id'] for t in tasks) + 1

# add expense with a description and amount.
def add(argv):
    if "--description" not in argv or "--amount" not in argv:
        print("Usage: add --description <text> --amount <number>")
        return

    try:
        description = argv[argv.index("--description") + 1]
        amount = argv[argv.index("--amount") + 1]
        amount = float(amount)
    except (ValueError, IndexError):
        print("Invalid description or amount.")
        return

    expenses = load_expense()
    id = new_id(expenses)
    now = datetime.now().strftime("%Y-%m-%d")

    new_expense = {
        'id': id,
        'date': now,
        'description': description,
        'amount': f"{amount:.2f}"
    }
    expenses.append(new_expense)
    with open(JSON_FILE, "w") as f:
        json.dump(expenses, f, indent=4)
    print(f"Expense added successfully (ID: {id})")

# update an expense (with id)
def update(argv):
    if "--id" not in argv:
        print("Usage: update --id <number> --description <text> --amount <number>")
        return
    try:
        id = int(argv[argv.index("--id") + 1])
    except (ValueError, IndexError):
        print("Invalid ID format")
        return

    if "--description" in argv:
        try:
            description = argv[argv.index("--description") + 1]
        except IndexError:
            description = ""
    else:
        description = ""

    if "--amount" in argv:
        try:
            amount = argv[argv.index("--amount") + 1]
            amount = float(amount)
            amount = f"{amount:.2f}"
        except (ValueError, IndexError):
            amount = ""
    else:
        amount = ""

    if not description and not amount:
        print("No description or amount provided.")
        return

    expenses = load_expense()
    found = False

    for expense in expenses:
        if expense["id"] == id:
            if description:
                expense["description"] = description
            if amount:
                expense["amount"] = amount
            found = True
            break
        
    if found:
        with open(JSON_FILE, "w") as f:
            json.dump(expenses, f, indent=4)
        print(f"Task with ID {id} updated.")
    else:
        print("ID not found")


# delete an expense (with id)
def delete(argv):
    if "--id" not in argv:
        print("Usage: delete --id <number>")
        return
    try:
        id = int(argv[argv.index("--id") + 1])
    except (ValueError, IndexError):
        print("Invalid ID format")
        return

    expenses = load_expense()
    original_len = len(expenses)
    expense = [exp for exp in expenses if exp["id"] != id]

    if len(expense) < original_len:
        with open(JSON_FILE, "w") as f:
            json.dump(expense, f, indent=4)
        print(f"Expense deleted successfully")
    else:
        print("ID not found.")

# view all expenses
def viewAll():
    expenses = load_expense()

    if not expenses:
        print("no expense")
        return
    
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':>8}")
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} {expense['amount']:>8}")


#summary
def summary():
    argv = sys.argv
    expenses = load_expense()

    # Detect optional filters
    month = None
    year = datetime.now().strftime("%Y")  # Default year

    if "--month" in argv:
        try:
            month_index = argv.index("--month") + 1
            month = argv[month_index].zfill(2)  # Format as '08', '12', etc.
        except IndexError:
            print("Please provide a valid month number after --month")
            return

    if "--year" in argv:
        try:
            year_index = argv.index("--year") + 1
            year = argv[year_index]
        except IndexError:
            print("Please provide a valid year after --year")
            return

    if month:
        expenses = [
            exp for exp in expenses
            if exp["date"].startswith(f"{year}-{month}")
        ]
        if not expenses:
            print(f"No expenses found for {year}-{month}")
            return
        month_name = datetime.strptime(month, "%m").strftime("%B")
        print(f"# Total expenses for {month_name} {year}:")
    elif "--year" in argv:
        expenses = [
            exp for exp in expenses
            if exp["date"].startswith(f"{year}-")
        ]
        if not expenses:
            print(f"No expenses found for {year}")
            return
        print(f"# Total expenses for {year}:")
    else:
        print("\n# Total expenses:")

    amounts = [float(exp["amount"]) for exp in expenses]
    total = sum(amounts)
    print(f"${total:.2f}")


def main():
    argv = sys.argv

    command = argv[1]

    if command == "add":
        add(argv)
    elif command == "list":
        viewAll()
    elif command == 'update':
        update(argv)
    elif command == 'delete':
        delete(argv)
    elif command == "summary":
        summary()
    else:
        print("Unknown command. Available commands: add, list, update, delete, summary, view")
if __name__ == "__main__":
    main()
