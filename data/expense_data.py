class ExpenseData:
    def __init__(self):
        self.expenses = []
        self.observers = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.notify_observers()

    def get_expenses(self):
        return self.expenses

    def clear_expenses(self):
        self.expenses = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer()