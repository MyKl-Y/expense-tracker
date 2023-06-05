import tkinter as tk
from tkinter import ttk

class Reporting(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Reporting")
        self.report_button = ttk.Button(self, text="Generate Report")

        self.setup_ui()

    def setup_ui(self):
        self.report_button.pack(padx=5, pady=5)
