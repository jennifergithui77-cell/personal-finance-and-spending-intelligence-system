# ============================================================
# PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM
# ============================================================


# ============================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================

import pandas as pd


# ============================================================
# STEP 2: LOAD THE DATASET
# ============================================================

# Load the CSV file into a pandas DataFrame.
# A DataFrame is a table containing rows and columns.

df = pd.read_csv("data/raw/Personal_Finance_Dataset.csv")

print("=" * 60)
print("STEP 2: DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst five transactions:")
print(df.head())


# ============================================================
# STEP 3: EXPLORE THE DATASET
# ============================================================

print("\n" + "=" * 60)
print("STEP 3: DATASET EXPLORATION")
print("=" * 60)

# Display the number of rows and columns.
print("\nDataset dimensions:")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# Display the column names.
print("\nColumn names:")
print(df.columns.tolist())

# Display information about the columns and their data types.
print("\nDataset information:")
df.info()

# Display the first five records.
print("\nFirst five records:")
print(df.head())

# Display the last five records.
print("\nLast five records:")
print(df.tail())


# ============================================================
# STEP 4: CHECK DATA QUALITY
# ============================================================

print("\n" + "=" * 60)
print("STEP 4: DATA QUALITY CHECKS")
print("=" * 60)

# Check the number of missing values in each column.
print("\nMissing values per column:")
print(df.isnull().sum())

# Calculate the total number of missing values.
total_missing = df.isnull().sum().sum()

print(f"\nTotal missing values: {total_missing}")

# Check for completely duplicated rows.
duplicate_rows = df.duplicated().sum()

print(f"\nNumber of duplicate rows: {duplicate_rows}")

# Check for duplicated customer transaction descriptions and
# dates only if needed in a future analysis.
# We do not remove records based on descriptions because
# different transactions can have similar descriptions.

# Check for zero amounts.
zero_amounts = (df["Amount"] == 0).sum()

print(f"\nNumber of zero-amount transactions: {zero_amounts}")

# Check for negative amounts.
negative_amounts = (df["Amount"] < 0).sum()

print(f"Number of negative-amount transactions: {negative_amounts}")

# Display the number of transactions in each category.
print("\nTransaction counts by category:")
print(df["Category"].value_counts())

# Display the number of transactions by type.
print("\nTransaction counts by type:")
print(df["Type"].value_counts())


# ============================================================
# STEP 5: PREPARE THE DATA
# ============================================================

print("\n" + "=" * 60)
print("STEP 5: DATA PREPARATION")
print("=" * 60)

# Convert the Date column from text into datetime values.
# Invalid dates, if any, will become missing datetime values.

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Count dates that could not be converted.
invalid_dates = df["Date"].isna().sum()

print("\nDate column converted to datetime format.")

print(f"Invalid or missing dates after conversion: {invalid_dates}")

# Display the data types after preparation.
print("\nUpdated column data types:")
print(df.dtypes)

# Display the earliest and latest valid dates.
if df["Date"].notna().any():

    earliest_date = df["Date"].min()
    latest_date = df["Date"].max()

    print(f"\nEarliest transaction date: {earliest_date.date()}")
    print(f"Latest transaction date: {latest_date.date()}")

else:
    print("\nNo valid dates are available for analysis.")


# ============================================================
# STEP 6: EXAMINE TRANSACTION CATEGORIES AND TYPES
# ============================================================

print("\n" + "=" * 60)
print("STEP 6: TRANSACTION CATEGORIES AND TYPES")
print("=" * 60)

# List all unique transaction categories.
categories = df["Category"].dropna().unique()

print("\nAvailable transaction categories:")
for category in sorted(categories):
    print(f"- {category}")

# Count transactions in each category.
category_counts = df["Category"].value_counts()

print("\nNumber of transactions in each category:")
print(category_counts.to_string())

# Examine the types of transactions.
transaction_types = df["Type"].value_counts()

print("\nNumber of transactions by type:")
print(transaction_types.to_string())


# ============================================================
# STEP 7: DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("STEP 7: DESCRIPTIVE STATISTICS")
print("=" * 60)

# Calculate summary statistics for the Amount column.
# These include count, mean, standard deviation, minimum,
# quartiles and maximum.

print("\nSummary statistics for transaction amounts:")
print(df["Amount"].describe())

# Calculate the total transaction amount.
total_transaction_amount = df["Amount"].sum()

# Calculate the average transaction amount.
average_transaction_amount = df["Amount"].mean()

# Find the smallest and largest transaction amounts.
smallest_transaction = df["Amount"].min()
largest_transaction = df["Amount"].max()

print("\nAdditional transaction statistics:")

print(f"Total transaction amount: {total_transaction_amount:,.2f}")

print(
    f"Average transaction amount: "
    f"{average_transaction_amount:,.2f}"
)

print(f"Smallest transaction amount: {smallest_transaction:,.2f}")

print(f"Largest transaction amount: {largest_transaction:,.2f}")


# ============================================================
# STEP 8: DATASET SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("STEP 8: DATASET SUMMARY")
print("=" * 60)

# Count all transactions.
total_transactions = len(df)

# Count distinct categories.
number_of_categories = df["Category"].nunique()

# Count distinct transaction types.
number_of_transaction_types = df["Type"].nunique()

print(f"\nTotal number of transactions: {total_transactions}")

print(f"Number of transaction categories: {number_of_categories}")

print(f"Number of transaction types: {number_of_transaction_types}")

print(f"Total missing values: {df.isnull().sum().sum()}")

print(f"Total duplicate rows: {df.duplicated().sum()}")

print("\nSteps 1–8 completed successfully!")

# ============================================================
# STEP 9: INCOME AND EXPENSE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("STEP 9: INCOME AND EXPENSE ANALYSIS")
print("=" * 60)

# 1. Select income transactions

income_transactions = df[df["Type"] == "Income"]

# 2. Calculate total income

total_income = income_transactions["Amount"].sum()

# 3. Select expense transactions

expense_transactions = df[df["Type"] == "Expense"]

# 4. Calculate total expenses

total_expenses = expense_transactions["Amount"].sum()

# 5. Calculate the difference between income and expenses

income_expense_difference = total_income - total_expenses

# 6. Count income and expense transactions

number_of_income_transactions = len(income_transactions)

number_of_expense_transactions = len(expense_transactions)

# 7. Calculate average transaction amounts

average_income = income_transactions["Amount"].mean()

average_expense = expense_transactions["Amount"].mean()

# 8. Display the results

print(f"\nTotal income: {total_income:,.2f}")

print(f"Total expenses: {total_expenses:,.2f}")

print(f"Income minus expenses: {income_expense_difference:,.2f}")

print(
    f"\nNumber of income transactions: "
    f"{number_of_income_transactions}"
)

print(
    f"Number of expense transactions: "
    f"{number_of_expense_transactions}"
)

print(f"\nAverage income transaction: {average_income:,.2f}")

print(f"Average expense transaction: {average_expense:,.2f}")

# 9. Interpret the difference

if income_expense_difference > 0:
    print("\nInterpretation: Recorded income exceeds recorded expenses.")

elif income_expense_difference < 0:
    print("\nInterpretation: Recorded expenses exceed recorded income.")

else:
    print("\nInterpretation: Recorded income equals recorded expenses.")

print("\nIncome and expense analysis completed successfully!")

# ============================================================
# STEP 10: SPENDING ANALYSIS BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("STEP 10: SPENDING ANALYSIS BY CATEGORY")
print("=" * 60)

# 1. Group expense transactions by category.
# 2. Add the amounts within each category.
# 3. Sort the results from highest to lowest spending.

category_spending = (
    expense_transactions.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Display total spending for every category.

print("\nTotal expenses by category:")
print(category_spending.to_string())

# Identify the category with the highest spending.

highest_category = category_spending.idxmax()
highest_amount = category_spending.max()

print("\nHIGHEST-SPENDING CATEGORY:")
print(f"Category: {highest_category}")
print(f"Total amount: {highest_amount:,.2f}")

# Identify the category with the lowest spending.

lowest_category = category_spending.idxmin()
lowest_amount = category_spending.min()

print("\nLOWEST-SPENDING CATEGORY:")
print(f"Category: {lowest_category}")
print(f"Total amount: {lowest_amount:,.2f}")

print("\nSpending analysis by category completed successfully!")

# ============================================================
# STEP 11: VISUALIZE SPENDING BY CATEGORY
# ============================================================

# Import matplotlib for creating charts.
import matplotlib.pyplot as plt

print("\n" + "=" * 60)
print("STEP 11: SPENDING BY CATEGORY VISUALIZATION")
print("=" * 60)

# Create a bar chart using the category totals calculated
# in Step 10.

plt.figure(figsize=(12, 6))

category_spending.plot(
    kind="bar",
    title="Total Expenses by Category",
    xlabel="Transaction Category",
    ylabel="Total Expenses",
)

# Rotate category labels so they are easier to read.
plt.xticks(rotation=45, ha="right")

# Adjust the layout to prevent labels from being cut off.
plt.tight_layout()

# Display the chart.
plt.show()

print("\nSpending visualization completed successfully!")

# ============================================================
# STEP 12: INVESTIGATE SALARY CLASSIFICATION
# ============================================================

print("\n" + "=" * 60)
print("STEP 12: INVESTIGATE SALARY CLASSIFICATION")
print("=" * 60)

# Select all transactions in the Salary category.
salary_transactions = df[df["Category"] == "Salary"]

# Count how these transactions are classified.
print("\nSalary transactions by transaction type:")
print(salary_transactions["Type"].value_counts())

# Display a sample of Salary transactions.
print("\nSample Salary transactions:")
print(
    salary_transactions[
        ["Date", "Transaction Description", "Category", "Amount", "Type"]
    ].head(10)
)

print("\nSalary classification investigation completed!")

# ============================================================
# STEP 13: INVESTIGATE TRANSACTION CATEGORIES
# ============================================================

print("\n" + "=" * 60)
print("STEP 13: INVESTIGATE TRANSACTION CATEGORIES")
print("=" * 60)

# Count transactions for each combination of category and type.
category_type_counts = pd.crosstab(
    df["Category"],
    df["Type"]
)

print("\nTransaction counts by category and type:")
print(category_type_counts)

# Calculate the total amount for each category and type.
category_type_amounts = pd.pivot_table(
    df,
    values="Amount",
    index="Category",
    columns="Type",
    aggfunc="sum",
    fill_value=0
)

print("\nTotal transaction amounts by category and type:")
print(category_type_amounts.round(2))

print("\nCategory investigation completed successfully!")

# ============================================================
# STEP 14: MONTHLY EXPENSE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("STEP 14: MONTHLY EXPENSE ANALYSIS")
print("=" * 60)

# Select transactions classified as expenses.
expense_transactions = df[df["Type"] == "Expense"].copy()

# Extract the year and month from each transaction date.
expense_transactions["Year_Month"] = (
    expense_transactions["Date"].dt.to_period("M")
)

# Calculate the total expenses recorded each month.
monthly_expenses = (
    expense_transactions
    .groupby("Year_Month")["Amount"]
    .sum()
    .sort_index()
)

# Display monthly expense totals.
print("\nTotal recorded expenses by month:")
print(monthly_expenses.to_string())

# Identify the month with the highest recorded expenses.
highest_spending_month = monthly_expenses.idxmax()
highest_month_amount = monthly_expenses.max()

print("\nMONTH WITH THE HIGHEST RECORDED EXPENSES:")
print(f"Month: {highest_spending_month}")
print(f"Total: {highest_month_amount:,.2f}")

# Identify the month with the lowest recorded expenses.
lowest_spending_month = monthly_expenses.idxmin()
lowest_month_amount = monthly_expenses.min()

print("\nMONTH WITH THE LOWEST RECORDED EXPENSES:")
print(f"Month: {lowest_spending_month}")
print(f"Total: {lowest_month_amount:,.2f}")

print("\nMonthly expense analysis completed successfully!")

# ============================================================
# STEP 15: VISUALISE MONTHLY EXPENSES
# ============================================================

import matplotlib.pyplot as plt

print("\n" + "=" * 60)
print("STEP 15: MONTHLY EXPENSE VISUALIZATION")
print("=" * 60)

# Create a figure for the line chart.
plt.figure(figsize=(14, 6))

# Plot monthly expenses over time.
plt.plot(
    monthly_expenses.index.astype(str),
    monthly_expenses.values,
    marker="o",
    linestyle="-"
)

# Add a descriptive title and axis labels.
plt.title("Monthly Recorded Expenses (2020–2024)")
plt.xlabel("Month")
plt.ylabel("Total Recorded Expenses")

# Display fewer date labels so they remain readable.
plt.xticks(
    ticks=range(0, len(monthly_expenses), 3),
    labels=monthly_expenses.index.astype(str)[::3],
    rotation=45,
    ha="right"
)

# Add a grid to make values easier to compare.
plt.grid(True, alpha=0.3)

# Adjust spacing to prevent labels from being cut off.
plt.tight_layout()

# Display the chart.
plt.show()

print("\nMonthly expense visualization completed successfully!")

