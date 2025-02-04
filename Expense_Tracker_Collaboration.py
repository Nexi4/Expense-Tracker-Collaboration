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
#--------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------
