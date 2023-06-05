import tkinter as tk
from tkinter import ttk

class DataIO(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Data Export/Import")
        self.export_button = ttk.Button(self, text="Export Data")
        self.import_button = ttk.Button(self, text="Import Data")

        self.setup_ui()

    def setup_ui(self):
        self.export_button.pack(padx=5, pady=5)
        self.import_button.pack(padx=5, pady=5)
