"""
    Income models for bodjeban project.
    مدل‌های مربوط به درآمد برای پروژه بوجبان

    - IncomeIn: مدل ورودی برای ثبت درآمد جدید
    - IncomeOut: مدل خروجی برای نمایش درآمدها با فیلدهای اضافی مثل شناسه و زمان ایجاد
"""

# models/income_model.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class IncomeIn(BaseModel):
    """
    مدل ورودی درآمد (IncomeIn) برای گرفتن داده‌های ورودی از کاربر

    ویژگی‌ها:
    - title: عنوان درآمد (مثلاً "حقوق")
    - amount: مبلغ درآمد به صورت عدد اعشاری
    - date: تاریخ و زمان درآمد به صورت datetime استاندارد ISO8601
    - description: توضیح اختیاری درباره درآمد
    """
    title: str = Field(..., examples=["salary"])
    amount: float = Field(..., examples=[10000000])
    date: datetime = Field(..., examples=["2025-05-17T12:00:00"])
    description: Optional[str] = Field(None, examples=["Monthly salary"])

class IncomeOut(IncomeIn):
    """
    مدل خروجی درآمد (IncomeOut) که داده‌های کامل‌تر شامل شناسه و زمان ایجاد را نمایش می‌دهد.

    این مدل از IncomeIn ارث‌بری می‌کند و دو فیلد اضافه دارد:
    - id: شناسه یکتای درآمد (معمولاً از دیتابیس)
    - created_at: زمان ثبت درآمد در سیستم
    """
    id: str
    created_at: datetime
