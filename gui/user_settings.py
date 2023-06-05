import tkinter as tk
from tkinter import ttk

class UserSettings(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="User Settings")
        self.theme_combobox = ttk.Combobox(self, values=["Light", "Dark"])
        self.theme_combobox.current(0)

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self, text="Theme:").grid(row=0, column=0, padx=5, pady=5)
        self.theme_combobox.grid(row=0, column=1, padx=5, pady=5)
