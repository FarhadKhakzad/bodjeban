from fastapi import APIRouter
from pydantic import BaseModel
from database import add_expense, get_expenses, get_expense, update_expense, delete_expense

router = APIRouter()

# مدل Pydantic برای ورودی‌ها
class ExpenseSchema(BaseModel):
    user_id: str
    day: str
    date: str
    title: str
    amount: float
    description: str = ""

# ایجاد هزینه جدید
@router.post("/expenses/")
def create_expense(expense: ExpenseSchema):
    return add_expense(**expense.model_dump())

# دریافت همه هزینه‌ها
@router.get("/expenses/")
def read_expenses():
    return get_expenses()

# دریافت یک هزینه خاص
@router.get("/expenses/{expense_id}")
def read_expense(expense_id: str):
    return get_expense(expense_id)

# ویرایش هزینه
@router.put("/expenses/{expense_id}")
def modify_expense(expense_id: str, expense: ExpenseSchema):
    return update_expense(expense_id, **expense.model_dump())

# حذف هزینه
@router.delete("/expenses/{expense_id}")
def remove_expense(expense_id: str):
    return delete_expense(expense_id)
