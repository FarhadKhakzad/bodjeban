"""
    Routes for income management in bodjeban project.
    مسیرهای مربوط به درآمدها در پروژه بودجبان
"""

# routes/income.py

from datetime import datetime
from fastapi import APIRouter, HTTPException

from app.models.income_model import IncomeIn, IncomeOut
from app.database import db

router = APIRouter()

@router.post("/income")

async def create_income(income: IncomeIn):
    """
    Create a new income entry.
    """

    income_dict = income.dict()
    income_dict["created-at"] = datetime.utcnow()
    result = await db["incomes"].insert_one(income_dict)
    income_dict["id"] = str(result.inserted_id)
    return IncomeOut(
        id=str(result.inserted_id),
        created_at=income_dict["created_at"],
        **income_dict
    )
