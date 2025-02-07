# Empty dictionary
expense_listings = {}
from datetime import datetime
on = True
categories = ["Food", "Clothing", "Utility", "Entertainment", "Transport", "Healthcare", "Insurance", "Housing", "Internet", "Other"]
def main_menu():
    global on
    while on:
        choice = input("Choose one of the options: \n1) Add Expense\n2) View Expense\n3) Total Expense\n4) Filter Expens\n5) Delete Expense\n6) Exit\n")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            filter_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            on = False
def total_expense():
    total = 0
    for expenses in expense_listings.values():
        for expense in expenses:
            total += expense["Amount spent"]
    print(f"Your total expenses is: ${total:.2f}")
def add_expense():
    while True:
        expense_category = input(f"Add what kind of expense?\n Choose from {categories} ").capitalize()
        if expense_category not in categories:
            print("Not in the category list, choose again.")
            continue
        elif expense_category == "Other":
            new_category = input("What category do you want to add?: ").capitalize()
            categories.append(new_category)
            expense_category = new_category
            break
        else:
            break

    while True:
        try:
            expense_amount = float(input("How much? "))
            break
        except ValueError:
            print("Not a number, try again.")

    while True:
            date_attempt = input("When was the expense(YYYY-MM-DD)?: ")
            try:
                expense_time = datetime.strptime(date_attempt, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Enter time in given format.")

    if expense_category not in expense_listings:
        expense_listings[expense_category] = []

    expense_listings[expense_category].append({
        'Amount spent': expense_amount,
        'Time of expense': expense_time
        })

    print(f"Expense added:\n {expense_category}: Spent ${expense_amount} on {expense_time}")

def view_expense():
    if not expense_listings:
        print("No expenses yet.")
        return
    
    for expense_category, expenses in expense_listings.items():
        print("---------Expenses----------")
        print(f"\nCategory: {expense_category}")
        for expense in expenses:
            
            print(f" Amount: ${expense['Amount spent']}\n Time: {expense['Time of expense']}\n")
            print("---------------------------")
 

def filter_expenses(category=None, date=None, min_amount=None, max_amount=None):
    filtered = []
    
    for expense_category, expenses in expense_listings.items():
        if category and category != expense_category:
            continue
        
        for expense in expenses:
            if date and expense["Time of spending"] != date:
                continue
            if min_amount and expense["Amount spent"] < min_amount:
                continue
            if max_amount and expense["Amount spent"] > max_amount:
                continue
            
            filtered.append({"category": expense_category, **expense})
    
    return filtered

def delete_expense(category, index):
    if category not in expense_listings:
        print(f"Category '{category}' not found.")
        return False

    if index < 0 or index >= len(expense_listings[category]):
        print(f"Invalid index: {index}. No expense deleted.")
        return False

    deleted_expense = expense_listings[category].pop(index)
    print(f"Deleted expense: {deleted_expense}")
    return True
main_menu()
