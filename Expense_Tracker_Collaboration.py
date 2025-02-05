expense_listings = {}
from datetime import datetime
on = True
def main_menu():
    global on
    while on:
        choice = input("Choose one of the options: \n1) Add Expense\n2) View Expense\n3) Total Expense\n4) Delete Expense\n5) Exit\n")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            pass
        elif choice == '5':
            on = False

def add_expense():
        categories = ["Food", "Clothing", "Utility", "Entertainment", "Transport", "Healthcare", "Insurance", "Housing", "Internet", "Other\n"]
        while True:
            expense_category = input(f"Add what kind of expense?\n Choose from {categories} ").capitalize()
            if expense_category not in categories:
                print("Not in the category list, choose again.")
                continue
            elif expense_category == "Other":
                specified_category = input("What category do you want to add?: ").capitalize()
                categories.append(specified_category)
                expense_category = specified_category
                break
            else:
                break

        try:
            expense_amount = float(input("How much? "))
        except ValueError:
            print("Not a number, try again.")
            return

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

        print(f"Expense added:\n {expense_category}: Spent ${expense_amount} on {expense_time}\n")

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
 
def total_expense():
    pass

main_menu()
