from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.functions import return_all_expenses, save_return_expenses
from app.models import Expense

app = FastAPI(title="Expense Management Application",
              description="Expense Management Application to track expense and manage their financial activites",
              version="0.0.1")


@app.post("/api/v1/expenses/")
def expenses(expenses: Expense):
    """
    1. API takes in expense data
    2. Calls save_return_expenses function to save expense data
    3. Returns saved data in JSON format
    """
    try:
        saved_data = save_return_expenses(expenses)
        return JSONResponse(content = saved_data, status_code=200)
    except Exception as e:
        return JSONResponse(content=str(e), status_code=400)

@app.get("/api/v1/expenses/")
async def get_all_expenses():
    """
    1. Calls return_all_expenses function
    2. Returns all expenses data in JSON format
    """
    try:
        all_data = await return_all_expenses()
        return JSONResponse(content= all_data, status_code=200)
    except Exception as e:
        return JSONResponse(content=str(e), status_code=400)


@app.get("/api/v1/expenses/month/{year}/{month}/")
def get_expenses_by_month(year: int, month: int):
    pass


@app.get("/api/v1/expenses/totals/")
def get_total_expenses():
    pass