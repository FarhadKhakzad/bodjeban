import os
from supabase import create_client, client
from dotenv import load_dotenv
import uuid

# بارگذاری متغیرهای محیطی
load_dotenv()

# دریافت مقادیر از .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ایجاد کلاینت Supabase
supabase: client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("✅ اتصال به Supabase برقرار شد!")

def add_expense(user_id, day, date, title, amount, description=""):
    data = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "day": day,
        "date": date,
        "title": title,
        "amount": amount,
        "description": description
    }
    response = supabase.table("expenses").insert(data).execute()
    return response

def get_expenses():
    response = supabase.table("expenses").select("*").execute()
    return response.data

def get_expense(expense_id):
    response = supabase.table("expenses").select("*").eq("id", expense_id).execute()
    return response.data

def update_expense(expense_id, day=None, date=None, title=None, amount=None, description=None):
    data = {}
    if day is not None:
        data["day"] = day
    if date is not None:
        data["date"] = date
    if title is not None:
        data["title"] = title
    if amount is not None:
        data["amount"] = amount
    if description is not None:
        data["description"] = description

    if not data:  # اگر هیچ داده‌ای برای بروزرسانی وجود نداشته باشد
        return {"error": "No data provided for update"}

    response = supabase.table("expenses").update(data).eq("id", expense_id).execute()
    return response.data

def delete_expense(expense_id):
    response = supabase.table("expenses").delete().eq("id", expense_id).execute()
    return response