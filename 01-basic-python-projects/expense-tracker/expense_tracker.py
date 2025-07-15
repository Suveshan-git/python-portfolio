import json
from datetime import datetime

# Load data
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, travel): ")
    date = input("Enter date (YYY-MM-DD) or press Enter for today: ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved!")

def view_expenses():
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: R{expense['amount']}")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")