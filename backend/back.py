# کلاس ثبت هزینه‌ها
class Expense:
    all_expenses = []

    def __init__(self, user_id, day, date, title, amount, description=""):
        self.id = None
        self.user_id = user_id
        self.day = day
        self.date = date
        self.title = title
        self.amount = amount
        self.description = description

    # ذخیره هزینه
    def save(self):
        Expense.all_expenses.append(self)

    # نمایش هزینه‌ها
    def __repr__(self):
        return f"Expense(id={self.id}, title={self.title}, amount={self.amount})"


# کلاس عملیات بر روی هزینه‌ها
class ExpenseService:
    expenses = []

    # متد اضافه کردن هزینه
    @classmethod
    def add_expense(cls, user_id, day, date, title, amount, description=""):
        expense = Expense(user_id, day, date, title, amount, description)
        expense.id = len(cls.expenses) + 1
        cls.expenses.append(expense)
        return expense

    # متد برگرداندن همه هزینه‌ها
    @classmethod
    def get_expenses(cls):
        return cls.expenses

    # متد برگرداندن یک هزینه خاص
    @classmethod
    def get_expense(cls, expense_id):
        for expense in cls.expenses:
            if expense.id == expense_id:
                return expense
        return None

    # متد ویرایش یک هزینه خاص
    @classmethod
    def update_expense(cls, expense_id, day=None, date=None, title=None, amount=None, description=None):
        for expense in cls.expenses:
            if expense.id == expense_id:
                if day is not None:
                    expense.day = day
                if date is not None:
                    expense.date = date
                if title is not None:
                    expense.title = title
                if amount is not None:
                    expense.amount = amount
                if description is not None:
                    expense.description = description
                return expense
        return None

    # متد حذف یک هزینه خاص
    @classmethod
    def delete_expense(cls, expense_id):
        for expense in cls.expenses:
            if expense.id == expense_id:
                cls.expenses.remove(expense)
                return True
        return False