from config import SUPABASE_URL, SUPABASE_KEY

import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# دریافت مقادیر از .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("SUPABASE_URL:", SUPABASE_URL)  # برای تست اینکه مقدار درست خوانده شده
print("SUPABASE_KEY:", SUPABASE_KEY)  # اینو می‌تونی بعداً حذف کنی
