import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data.expense_data import ExpenseData

class ExpenseInput(ttk.LabelFrame):
    def __init__(self, master, expense_data, expense_list, expense_analysis):
        super().__init__(master, text="Expense Input")
        self.date_entry = ttk.Entry(self)
        self.category_entry = ttk.Entry(self)
        self.amount_entry = ttk.Entry(self)
        self.add_button = ttk.Button(self, text="Add Expense", command=self.add_expense)

        self.expense_data = expense_data  # Create an instance of the ExpenseData class
        self.expense_list = expense_list  # Store the expense_list instance
        self.expense_analysis = expense_analysis

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self, text="Date:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button.grid(row=3, columnspan=2, padx=5, pady=5)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        # Validate the input fields
        if not date or not category or not amount:
            # Show an error message if any field is empty
            tk.messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Convert the amount to a float
        try:
            amount = float(amount)
        except ValueError:
            # Show an error message if the amount is not a valid number
            tk.messagebox.showerror("Error", "Invalid amount. Please enter a number.")
            return

        # Add the expense to the data model
        expense = {'date': date, 'category': category, 'amount': amount}
        self.expense_data.add_expense(expense)

        # Update the expense list (assuming you have an instance of the ExpenseList component)
        self.expense_list.update_expenses(self.expense_data.get_expenses())

        self.expense_analysis.update_chart()

        # Clear the input fields
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        # Show a success message
        tk.messagebox.showinfo("Success", "Expense added successfully.")
