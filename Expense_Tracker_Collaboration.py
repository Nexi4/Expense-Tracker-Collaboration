# Empty dictionary
expense_listings = {}
from datetime import datetime # For YYYY-MM-DD checks
on = True # for the 'while on' function
categories = ["Food", "Clothing", "Utility", "Entertainment", "Transport", "Healthcare", "Insurance", "Housing", "Internet", "Other"] # Set up catagories for adding expenses
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
            delete_expense()
        elif choice == '5':
            on = False
def total_expense():
    total = 0 
    for expenses in expense_listings.values(): # list through the dictiionary values and add them up
        for expense in expenses:
            total += expense["Amount spent"]
    print(f"Your total expenses is: ${total:.2f}") # print the result out
def add_expense():
    # Loops to maintain functionality in case of Error
    while True: 
        expense_category = input(f"Add what kind of expense?\n Choose from {categories} ").capitalize()
        if expense_category not in categories:
            print("Not in the category list, choose again.")
            # Resets back to catagory selection
            continue 
        #In case user chooses 'Other'
        elif expense_category == "Other":
            new_category = input("What category do you want to add?: ").capitalize()
            # Shoves added catagory into the list
            categories.append(new_category)
            # Just so that the code work without complications
            expense_category = new_category
            break
        else:
            break

    while True:
        try:
            # float just for decimals
            expense_amount = float(input("How much? "))
            break
        except ValueError:
            print("Not a number, try again.")

    while True:
            date_attempt = input("When was the expense(YYYY-MM-DD)?: ")
            # Ensures that the user input follows the YYYY-MM-DD
            try:
                expense_time = datetime.strptime(date_attempt, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Enter time in given format.")

    # Shoves new catagory into list, if not, just add date, time, and amount into the respective catagory
    if expense_category not in expense_listings:
        expense_listings[expense_category] = []

    expense_listings[expense_category].append({
        'Amount spent': expense_amount,
        'Time of expense': expense_time
        })
    # Say that expense is added
    print(f"Expense added:\n {expense_category}: Spent ${expense_amount} on {expense_time}")

def view_expense():
    # Check for any current expenses
    if not expense_listings:
        print("No expenses yet.")
        return
    
    # Organized viewing of expenses
    print("---------Expenses----------")
    for expense_category, expenses in expense_listings.items():
        print(f"\nCategory: {expense_category}")
        for expense in expenses:
            print(f" Amount: ${expense['Amount spent']}\n Time: {expense['Time of expense']}\n")
    
    print("---------------------------")
 

def delete_expense():
    if not expense_listings: # check the dictionary if there is anything to delete
        print("No expenses to delete.")
        return

    print("\nDelete expenses by:") 
    print("1) Category")
    print("2) Specific Date (within a category)")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        category = input("Enter the category to delete: ").capitalize() # let user input what category to delete and delete it from the dictionary
        if category in expense_listings:
            del expense_listings[category]
            print(f"All expenses in category '{category}' have been deleted.")
        else: # in case the user type in incorrectly or the category does not exist
            print("Category not found.")

    elif choice == '2':
        category = input("Enter the category: ").capitalize() # in case the user type in incorrectly or the category does not exist
        if category not in expense_listings:
            print("Category not found.")
            return
        
        date_attempt = input("Enter the date to delete expenses (YYYY-MM-DD): ") # let user enter the date in a YYYY-MM-DD format for comparison with the values in the dictionary to delete the value
        try:
            expense_date = datetime.strptime(date_attempt, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
            return

        expense_listings[category] = [expense for expense in expense_listings[category] if expense["Time of expense"] != expense_date]
        # delete the expense of that date
        print(f"Deleted expenses on {expense_date} from category '{category}'.")
main_menu()
