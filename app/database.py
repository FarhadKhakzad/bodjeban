""" 
    Database connection module for bodjeban project.
    ماژول اتصال به پایگاه داده برای پروژه بوجبان 
"""

# database.py

import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# MongoDB connection string
# رشته اتصال به MongoDB
mongo_url = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")

# Create a MongoDB client
# ایجاد یک کلاینت MongoDB
client = AsyncIOMotorClient(mongo_url)
db = client[db_name]
