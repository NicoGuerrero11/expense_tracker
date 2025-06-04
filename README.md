# Expense Tracker

A simple and efficient command-line Expense Tracker built with Python. This tool allows users to manage their personal finances by recording, updating, listing, and summarizing expenses — all via CLI commands.

## Features

- Add new expenses with a description, amount, and automatic date
- List all recorded expenses in a clear table format
- Update or delete expenses by ID
- View total expenses overall, by month, or by year
- Use simple flags for intuitive CLI interaction

## How to Use

Make sure you're in the project directory and run commands like so:

### ➕ Add Expense

```bash
python main.py add --description "Lunch" --amount 20
```

### 📃 List All Expenses

```bash
python main.py list
```

### ✏️ Update an Expense

```bash
python main.py update --id 1 --description "Dinner" --amount 25
```

### ❌ Delete an Expense

```bash
python main.py delete --id 2
```

### 📊 View Total Summary

```bash
python main.py summary
```

### 📅 View Summary by Month

```bash
python main.py summary --month 8
```

### 📆 View Summary by Year

```bash
python main.py summary --year 2024
```

### 🗓️ View Summary by Month and Year

```bash
python main.py summary --month 8 --year 2024
```

## Data Format

All expenses are stored in a local JSON file (`expenses.json`) using the following structure:

```json
{
  "id": 1,
  "description": "Lunch",
  "amount": "20.00",
  "date": "2024-08-12"
}
```

## Example Output

```bash
$ python main.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ python main.py list
# ID  Date        Description    Amount
# 1   2024-08-06  Lunch          $20.00

$ python main.py summary
# Total expenses: $20.00

$ python main.py summary --month 8
# Total expenses for August: $20.00
```

## Project Reference

This project is based on the Expense Tracker challenge from [roadmap.sh](https://roadmap.sh/projects/expense-tracker)
