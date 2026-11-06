# ============================================================
# PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM
# Exploratory Data Analysis: Expense Analysis
# ============================================================

from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# 1. DEFINE THE DATASET PATH
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "synthetic_financial_transactions.csv"
)


# ------------------------------------------------------------
# 2. LOAD THE DATASET
# ------------------------------------------------------------

df = pd.read_csv(DATA_FILE)

# Convert the Date column into datetime format.
df["Date"] = pd.to_datetime(df["Date"])

print("=" * 65)
print("PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM")
print("EXPENSE ANALYSIS")
print("=" * 65)

print(f"\nTotal transactions in dataset: {len(df):,}")


# ------------------------------------------------------------
# 3. FILTER EXPENSE TRANSACTIONS
# ------------------------------------------------------------

# Keep only transactions classified as expenses.
expense_df = df[df["Type"] == "Expense"].copy()

print("\nEXPENSE TRANSACTION OVERVIEW")
print("-" * 65)

print(f"Number of expense transactions: {len(expense_df):,}")

print(
    "Total recorded expenses: "
    f"KSh {expense_df['Amount'].sum():,.2f}"
)

print(
    "Average expense transaction: "
    f"KSh {expense_df['Amount'].mean():,.2f}"
)

print(
    "Median expense transaction: "
    f"KSh {expense_df['Amount'].median():,.2f}"
)


# ------------------------------------------------------------
# 4. ANALYSE EXPENSES BY CATEGORY
# ------------------------------------------------------------

expenses_by_category = (
    expense_df.groupby("Category")["Amount"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values(by="sum", ascending=False)
)

expenses_by_category.columns = [
    "Transaction_Count",
    "Total_Expenses_KSh",
    "Average_Expense_KSh",
    "Median_Expense_KSh",
]

# Calculate each category's percentage of total expenses.
expenses_by_category["Percentage_of_Total"] = (
    expenses_by_category["Total_Expenses_KSh"]
    / expense_df["Amount"].sum()
    * 100
)

print("\nEXPENSE ANALYSIS BY CATEGORY")
print("-" * 65)

print(expenses_by_category.round(2).to_string())


# ------------------------------------------------------------
# 5. IDENTIFY THE HIGHEST-SPENDING CATEGORIES
# ------------------------------------------------------------

print("\nTOP 5 EXPENSE CATEGORIES BY TOTAL AMOUNT")
print("-" * 65)

top_categories = expenses_by_category.head(5)

print(
    top_categories[
        ["Transaction_Count", "Total_Expenses_KSh", "Percentage_of_Total"]
    ].round(2).to_string()
)


# ------------------------------------------------------------
# 6. ANALYSE EXPENSES BY USER
# ------------------------------------------------------------

expenses_by_user = (
    expense_df.groupby("User_ID")["Amount"]
    .agg(["count", "sum", "mean"])
    .sort_values(by="sum", ascending=False)
)

expenses_by_user.columns = [
    "Expense_Transactions",
    "Total_Expenses_KSh",
    "Average_Expense_KSh",
]

print("\nEXPENSE ANALYSIS BY USER")
print("-" * 65)

print(expenses_by_user.round(2).to_string())


# ------------------------------------------------------------
# 7. ANALYSE MONTHLY EXPENSES
# ------------------------------------------------------------

# Create a Year-Month column for monthly grouping.
expense_df["Year_Month"] = (
    expense_df["Date"].dt.to_period("M")
)

monthly_expenses = (
    expense_df.groupby("Year_Month")["Amount"]
    .sum()
    .sort_index()
)

print("\nMONTHLY EXPENSE SUMMARY")
print("-" * 65)

print(f"Months with recorded expenses: {len(monthly_expenses)}")

print(
    "Average monthly expenses across the dataset: "
    f"KSh {monthly_expenses.mean():,.2f}"
)

print(
    "Highest total monthly expenses: "
    f"KSh {monthly_expenses.max():,.2f}"
)

print(
    "Lowest total monthly expenses: "
    f"KSh {monthly_expenses.min():,.2f}"
)


# ------------------------------------------------------------
# 8. CHECK EXPENSE CATEGORY DISTRIBUTION
# ------------------------------------------------------------

print("\nEXPENSE TRANSACTION COUNTS BY CATEGORY")
print("-" * 65)

print(
    expense_df["Category"]
    .value_counts()
    .to_string()
)


# ------------------------------------------------------------
# 9. FINAL NOTES
# ------------------------------------------------------------

print("\nANALYSIS NOTES")
print("-" * 65)

print("Dataset: Synthetic financial transactions.")
print("Currency: Kenyan Shillings (KSh).")
print("Only transactions classified as Expense are included.")
print("Savings transfers are excluded from expense calculations.")
print("Results describe fictional data, not actual Kenyan households.")

print("\nExpense analysis completed successfully.")

