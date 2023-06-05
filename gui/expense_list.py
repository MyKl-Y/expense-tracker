import tkinter as tk
from tkinter import ttk

class ExpenseList(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Expense List")
        self.expense_table = ttk.Treeview(self, columns=("Date", "Category", "Amount"))

        self.setup_ui()

    def setup_ui(self):
        self.expense_table.heading("Date", text="Date")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Amount", text="Amount")
        self.expense_table.pack()

    def update_expenses(self, expenses):
        # Clear existing items in the treeview
        self.expense_table.delete(*self.expense_table.get_children())

        # Insert expenses into the treeview
        for expense in expenses:
            self.expense_table.insert('', tk.END, values=(expense['date'], expense['category'], expense['amount']))

        # Adjust column widths
        self.expense_table.column('#0', width=0, stretch=tk.NO)
        self.expense_table.column('#1', width=100, anchor=tk.CENTER)
        self.expense_table.column('#2', width=150, anchor=tk.CENTER)
        self.expense_table.column('#3', width=100, anchor=tk.CENTER)

        # Set column headings
        self.expense_table.heading('#0', text='')
        self.expense_table.heading('#1', text='Date')
        self.expense_table.heading('#2', text='Category')
        self.expense_table.heading('#3', text='Amount')