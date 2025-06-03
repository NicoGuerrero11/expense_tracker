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
    description = "".join(argv[3])
    amount = "".join(argv[5])
    expenses = load_expense()
    id = new_id(expenses)
    now = datetime.now().strftime("%Y-%m-%d")

    new_expense = {
        'id': id,
        'date': now,
        'description': description,
        'amount': amount
    }
    expenses.append(new_expense)
    with open(JSON_FILE, "w") as f:
        json.dump(expenses, f, indent=4)
    print(f"\nExpense added successfully (ID: {id})")
# update an expense (with id)

def update():
    pass

# delete an expense (with id)

def delete():
    pass
# view a summary of all expenses

def viewAll():
    expenses = load_expense()

    if not expenses:
        print("no expense")
        return
    
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':>8}")
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} {expense['amount']:>8}")


# view a summary for a specific month (of current year)
def view():
    pass

def main():
    argv = sys.argv

    command = argv[1]

    if command == "add":
        add(argv)
    elif command == "list":
        viewAll()
if __name__ == "__main__":
    main()
