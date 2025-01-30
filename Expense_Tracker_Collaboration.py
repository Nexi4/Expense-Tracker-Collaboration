#Empty dictionary
expense_listings = {}

def add_expense():
    categories = ["Food", "Clothing", "Utility", "Entertainment", "Transport", "Healthcare", "Insurance", "Housing", "Internet", "Other"]
    while True:
        expense_category = input(f"Add what kind of expense?\n Choose from {categories} ").capitalize()
        if expense_category not in categories:
            print("Not in the category list, choose again.")
            continue
        else:
            break

    try:
        expense_amount = float(input("How much? "))
    except ValueError:
        print("Not a number, try again.")
        return

    expense_time = input("When was the expense? ")
    
    if expense_category not in expense_listings:
        expense_listings[expense_category] = []

        expense_listings[expense_category].append({
            'Amount spent': expense_amount,
            'Time of spending': expense_time
        })

    print(f"Expense added:\n {expense_category}: Spent ${expense_amount} on {expense_time}")

add_expense()
