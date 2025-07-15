import json
from datetime import datetime

# Try to load any exisiting data from the JSON file if any
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = [] # Create an empty list if nothing is found

# Function to add a new expense to the file
def add_expense():
    # Get the information for the amount, category and date for the expense
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, travel): ")
    date = input("Enter date (YYY-MM-DD) or press Enter for today: ")

    # Allow the user to just press enter to save the current date for the expense
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # Create a dictionary to save the expenses
    expense = {
        "amount": amount, 
        "category": category, 
        "date": date
        }

    # Add expense to the dictionary
    expenses.append(expense)

    # Save all expenses to the JSON file
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved!")

# Function to view all recorded expenses by looping through the dictionary
def view_expenses():
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: R{expense['amount']}")

# Main project loop that keeps running until the user exits
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense() # Call the add function
    elif choice == "2":
        view_expenses() # Call the view function
    elif choice == "3":
        break # Exit loop and end application
    else:
        print("Invalid choice.") # Handle any wrong inputs