import tkinter as tk
from tkinter import ttk

class Filtering(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Data Filtering")
        self.filter_combobox = ttk.Combobox(self, values=["All", "Food", "Transportation", "Entertainment"])
        self.filter_combobox.current(0)

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self, text="Filter by Category:").grid(row=0, column=0, padx=5, pady=5)
        self.filter_combobox.grid(row=0, column=1, padx=5, pady=5)
