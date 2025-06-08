"""
    Income models for bodjeban project.
    مدل‌های مربوط به درآمد برای پروژه بودجبان

    - IncomeIn: مدل ورودی برای ثبت درآمد جدید
    - IncomeOut: مدل خروجی برای نمایش درآمدها با فیلدهای اضافی مثل شناسه و زمان ایجاد
"""

# models/income_model.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
import jdatetime

class IncomeIn(BaseModel):
    """
    مدل ورودی درآمد (IncomeIn) برای گرفتن داده‌های ورودی از کاربر

    ویژگی‌ها:
    - title: عنوان درآمد (مثلاً "حقوق")
    - amount: مبلغ درآمد به صورت عدد اعشاری
    - date: تاریخ و زمان درآمد به صورت datetime، هم میلادی و هم شمسی پذیرفته می‌شود
    - description: توضیح اختیاری درباره درآمد
    """
    title: str = Field(..., examples=["حقوق"])
    amount: float = Field(..., examples=[10000000])
    date: datetime = Field(..., examples=["2025-06-10T14:00:00", "1404-03-20 14:00"])
    description: Optional[str] = Field(None, examples=["حقوق ماهانه"])

    @validator("date", pre=True)
    def check_date(cls, value):
        """
        اعتبارسنجی تاریخ: ابتدا سعی می‌کنیم به عنوان تاریخ شمسی تجزیه کنیم،
        در غیر این‌صورت آن را به عنوان تاریخ میلادی در نظر می‌گیریم.
        """
        if isinstance(value, datetime):
            return value
        try:
            # سعی در تبدیل تاریخ شمسی به میلادی
            jdt = jdatetime.datetime.strptime(value, "%Y-%m-%d %H:%M")
            return jdt.togregorian()
        except ValueError:
            # اگر تبدیل به شمسی نشد، فرض بر میلادی بودن است
            return datetime.fromisoformat(value)

class IncomeOut(IncomeIn):
    """
    مدل خروجی درآمد (IncomeOut) که داده‌های کامل‌تر شامل شناسه و زمان ایجاد را نمایش می‌دهد.

    این مدل از IncomeIn ارث‌بری می‌کند و دو فیلد اضافه دارد:
    - id: شناسه یکتای درآمد (معمولاً از دیتابیس)
    - created_at: زمان ثبت درآمد در سیستم
    """
    id: str
    created_at: datetime
