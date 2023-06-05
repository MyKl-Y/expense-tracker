import tkinter as tk
from tkinter import ttk

class BudgetManagement(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Budget Management")
        self.budget_entry = ttk.Entry(self)

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self, text="Budget Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.budget_entry.grid(row=0, column=1, padx=5, pady=5)
