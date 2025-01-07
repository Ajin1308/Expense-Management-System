import random


temp_storage = {}

def save_return_expenses(expenses):
    """
    1. Takes in expense data
    3. Updates the expense data with a random id (expense_id)
    2. Returns the stored expense data
    """
    r = random.randint(1, 1000)
    expense = expenses.update({"expense_id":r})
    temp_storage.update(expense)
    for key, values in temp_storage.items():
        if key == "expense_id":
            return {key, values}

def return_all_expenses():
    return temp_storage

def return_expense_by_month(year: int, month: int):
    pass