class Expense:
    Expense = []

    def __init__(self, id, user_id, day, date, title, amount, description=""):
        self.id = id
        self.user_id = user_id
        self.day = day
        self.date = date
        self.title = title
        self.amount = amount
        self.description = description

    def save(self):
        Expense.Expense.append(self)

    def __repr__(self):
        return f"Expense(id={self.id}, title={self.title}, amount={self.amount})" 
    
class ExpenseService:
    expenses = []

    @classmethod
    def add_expense(cls, expense):
        cls.expenses.append(expense)
    
