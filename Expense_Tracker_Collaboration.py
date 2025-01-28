def add_expense():
    categories = ["Food", "Clothing", "Utility", "Entertainment", "Transport", "Healthcare", "Insurance", "Housing", "Internet", "Other"]
    while True:
        expense_category = input(f"Add what kind of expense?\n Choose from {categories}")
        if expense_category not in categories:
            print("Not in the category list, choose again.")
            continue
        else:
            break
    expense_amount = int(input("How much?"))
    Expense = print(f"Spent ${expense_amount} on {expense_category}")
    

add_expense()
