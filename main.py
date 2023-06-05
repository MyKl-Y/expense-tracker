import tkinter as tk
from gui.expense_input import ExpenseInput
from gui.expense_list import ExpenseList
from gui.expense_analysis import ExpenseAnalysis
from gui.budget_management import BudgetManagement
from gui.reporting import Reporting
from gui.filtering import Filtering
from gui.data_io import DataIO
from gui.user_settings import UserSettings
from data.expense_data import ExpenseData

def main():
    root = tk.Tk()
    root.title("Expense Tracker")

    expense_list = ExpenseList(root)
    #expense_list.pack()

    expense_data = ExpenseData()

    expense_analysis = ExpenseAnalysis(root, expense_data)
    #expense_analysis.pack(side="right")

    expense_input = ExpenseInput(root, expense_data, expense_list, expense_analysis)
    #expense_input.pack()

    budget_management = BudgetManagement(root)
    #budget_management.pack()

    reporting = Reporting(root)
    #reporting.pack()

    filtering = Filtering(root)
    #filtering.pack()

    data_io = DataIO(root)
    #data_io.pack()

    user_settings = UserSettings(root)
    #user_settings.pack()

    expense_input.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    expense_list.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    expense_analysis.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
    budget_management.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    reporting.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
    filtering.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
    data_io.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
    user_settings.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()