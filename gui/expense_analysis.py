import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseAnalysis(ttk.LabelFrame):
    def __init__(self, master, expense_data):
        super().__init__(master, text="Expense Analysis")
        self.expense_data = expense_data
        self.chart_frame = ttk.Frame(self)
        self.chart_frame.pack(fill='both', expand=True)
        self.create_analysis_charts()
        self.expense_data.add_observer(self.update_chart)

    def create_analysis_charts(self):
        self.figure = plt.figure(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.dropdown = ttk.Combobox(self, values=["Pie Chart", "Bar Chart by Month", "Line Chart by Year",
                                                   "Bar Chart by Category", "Line Chart by Month-Category",
                                                   "Bar Chart by Category-Year"])
        self.dropdown.current(0)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_chart)
        self.dropdown.pack()

        self.chart = self.figure.add_subplot(111)
        """
        self.figure = plt.figure(figsize=(8, 5))

        # First subplot: Pie chart by category
        self.chart1 = self.figure.add_subplot(121)
        self.chart1.pie([0], labels=["No Data"], autopct="%1.1f%%")
        self.chart1.axis("equal")

        # Second subplot: Bar chart by month
        self.chart2 = self.figure.add_subplot(122)
        self.chart2.bar([], [])
        self.chart2.set_xlabel("Month")
        self.chart2.set_ylabel("Total Expense")

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        """


    def update_chart(self, event=None):
        chart_type = self.dropdown.get()
        self.chart.clear()
        expenses = self.expense_data.get_expenses()

        if expenses:
            years = []
            totals_by_year = []
            categories = []
            amounts = []
            months = []
            totals = []
            categories_years = []
            totals_by_category_year = []
            if chart_type == "Pie Chart":
                # Update the first chart: Pie chart by category
                for expense in expenses:
                    category = expense["category"]
                    amount = expense["amount"]

                    if category not in categories:
                        categories.append(category)
                        amounts.append(amount)
                    else:
                        index = categories.index(category)
                        amounts[index] += amount

                self.chart.clear()
                self.chart.pie(amounts, labels=categories, autopct="%1.1f%%")
                self.chart.axis("equal")
            elif chart_type == "Bar Chart by Month":
                # Update the second chart: Bar chart by month
                for expense in expenses:
                    month = expense["date"]
                    amount = expense["amount"]

                    if month not in months:
                        months.append(month)
                        totals.append(amount)
                    else:
                        index = months.index(month)
                        totals[index] += amount

                self.chart.clear()
                self.chart.bar(months, totals)
                self.chart.set_xlabel("Month")
                self.chart.set_ylabel("Total Expense")
                self.chart.set_xticklabels(months, rotation=45)
            elif chart_type == "Line Chart by Year":
                # Update the third chart: Line chart by year

                for expense in expenses:
                    year = expense["date"].split("/")[0]
                    amount = expense["amount"]

                    if year not in years:
                        years.append(year)
                        totals_by_year.append(amount)
                    else:
                        index = years.index(year)
                        totals_by_year[index] += amount

                self.chart.clear()
                self.chart.plot(years, totals_by_year)
                self.chart.set_xlabel("Year")
                self.chart.set_ylabel("Total Expense")

            elif chart_type == "Bar Chart by Category":
                # Update the fourth chart: Horizontal bar chart by category
                self.chart.clear()
                self.chart.barh(categories, amounts)
                self.chart.set_xlabel("Total Expense")
                self.chart.set_ylabel("Category")
            elif chart_type == "Line Chart by Month-Category":
                # Update the fifth chart: Line chart by month and category
                months_categories = []
                totals_by_month_category = []
                for expense in expenses:
                    month_category = expense["date"] + "-" + expense["category"]
                    amount = expense["amount"]

                    if month_category not in months_categories:
                        months_categories.append(month_category)
                        totals_by_month_category.append(amount)
                    else:
                        index = months_categories.index(month_category)
                        totals_by_month_category[index] += amount

                self.chart.clear()
                self.chart.plot(months_categories, totals_by_month_category)
                self.chart.set_xlabel("Month-Category")
                self.chart.set_ylabel("Total Expense")
                self.chart.set_xticklabels(months_categories, rotation=45)
            elif chart_type == "Bar Chart by Category-Year":
                for expense in expenses:
                    category_year = expense["category"] + "-" + expense["date"].split("/")[0]
                    amount = expense["amount"]

                    if category_year not in categories_years:
                        categories_years.append(category_year)
                        totals_by_category_year.append(amount)
                    else:
                        index = categories_years.index(category_year)
                        totals_by_category_year[index] += amount

                self.chart.clear()
                self.chart.bar(categories_years, totals_by_category_year)
                self.chart.set_xlabel("Category-Year")
                self.chart.set_ylabel("Total Expense")
                self.chart.set_xticklabels(categories_years, rotation=45)
        else:
            if chart_type == "Pie Chart":
                self.chart.clear()
                self.chart.pie([0], labels=["No Data"], autopct="%1.1f%%")
                self.chart.axis("equal")
            elif chart_type == "Bar Chart by Month":
                self.chart.clear()
                self.chart.bar([], [])
                self.chart.set_xlabel("Month")
                self.chart.set_ylabel("Total Expense")
            elif chart_type == "Line Chart by Year":
                self.chart.clear()
                self.chart.plot([], [])
                self.chart.set_xlabel("Year")
                self.chart.set_ylabel("Total Expense")
            elif chart_type == "Bar Chart by Category":
                self.chart.clear()
                self.chart.barh([], [])
                self.chart.set_xlabel("Total Expense")
                self.chart.set_ylabel("Category")
            elif chart_type == "Line Chart by Month-Category":
                self.chart.clear()
                self.chart.plot([], [])
                self.chart.set_xlabel("Month-Category")
                self.chart.set_ylabel("Total Expense")
            elif chart_type == "Bar Chart by Category-Year":
                self.chart.clear()
                self.chart.bar([], [])
                self.chart.set_xlabel("Category-Year")
                self.chart.set_ylabel("Total Expense")

        self.canvas.draw()
        """
        expenses = self.expense_data.get_expenses()

        if expenses:
            # Update the first chart: Pie chart by category
            categories = []
            amounts = []
            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category not in categories:
                    categories.append(category)
                    amounts.append(amount)
                else:
                    index = categories.index(category)
                    amounts[index] += amount

            self.chart1.clear()
            self.chart1.pie(amounts, labels=categories, autopct="%1.1f%%")
            self.chart1.axis("equal")

            # Update the second chart: Bar chart by month
            months = []
            totals = []
            for expense in expenses:
                month = expense["date"]  # Assuming the date is already a string
                amount = expense["amount"]

                if month not in months:
                    months.append(month)
                    totals.append(amount)
                else:
                    index = months.index(month)
                    totals[index] += amount

            self.chart2.clear()
            self.chart2.bar(months, totals)
            self.chart2.set_xlabel("Month")
            self.chart2.set_ylabel("Total Expense")
            self.chart2.set_xticklabels(months, rotation=45)

        else:
            self.chart1.clear()
            self.chart1.pie([0], labels=["No Data"], autopct="%1.1f%%")
            self.chart1.axis("equal")

            self.chart2.clear()
            self.chart2.bar([], [])
            self.chart2.set_xlabel("Month")
            self.chart2.set_ylabel("Total Expense")

        self.canvas.draw()
        """