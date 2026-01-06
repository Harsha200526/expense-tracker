# Personal Expense Tracker

expenses = []  # list of dictionaries

def add_expense():
    category = input("Enter expense category: ")
    amou5nt = float(input("Enter amount: "))
    expense = {
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total amount spent: ₹{total}\n")

def highest_expense():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    highest = max(expenses, key=lambda x: x["amount"])
    print("Highest Expense:")
    print(f"Category: {highest['category']}, Amount: ₹{highest['amount']}\n")

def view_by_category():
    category = input("Enter category to view: ")
    found = False
    print(f"Expenses in category '{category}':")
    for exp in expenses:
        if exp["category"].lower() == category.lower():
            print(f"₹{exp['amount']}")
            found = True
    if not found:
        print("No expenses found in this category.")
    print()

def show_all_expenses():
    if not expenses:
        print("No expenses to show.\n")
        return
    print("All Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")
    print()

# Menu-driven program
while True:
    print("---- Personal Expense Tracker ----")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. View Highest Expense")
    print("4. View Expenses by Category")
    print("5. Show All Expenses")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        total_spent()
    elif choice == "3":
        highest_expense()
    elif choice == "4":
        view_by_category()
    elif choice == "5":
        show_all_expenses()
    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.\n")
