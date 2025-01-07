import random


temp_storage = {}

def save_return_expenses(expenses):
    """
    1. Takes in expense data
    3. Updates the expense data with a random id (expense_id)
    2. Returns the stored expense data
    """
    r = random.randint(1, 1000)
    temp_storage = temp_storage.update({"expense_id":r,{"name": expenses.name, "amount": expenses.amount, "category": expenses.category}})
    temp_storage.update(expense)
    return temp_storage

def return_all_expenses():
    return temp_storage

def return_expense_by_month(year: int, month: int):
    pass