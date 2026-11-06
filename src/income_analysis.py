# ============================================================
# PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM
# Exploratory Data Analysis: Income Analysis
# ============================================================

from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# 1. DEFINE THE DATASET PATH
# ------------------------------------------------------------

# Locate the main project directory.
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load the synthetic financial transactions dataset.
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

print("=" * 60)
print("PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM")
print("INCOME ANALYSIS")
print("=" * 60)

print(f"\nTotal transactions in dataset: {len(df):,}")


# ------------------------------------------------------------
# 3. FILTER INCOME TRANSACTIONS
# ------------------------------------------------------------

# Keep only transactions classified as Income.
income_df = df[df["Type"] == "Income"].copy()

print("\nINCOME TRANSACTION OVERVIEW")
print("-" * 60)

print(f"Number of income transactions: {len(income_df):,}")

print(
    "Total recorded income: "
    f"KSh {income_df['Amount'].sum():,.2f}"
)

print(
    "Average income transaction: "
    f"KSh {income_df['Amount'].mean():,.2f}"
)

print(
    "Median income transaction: "
    f"KSh {income_df['Amount'].median():,.2f}"
)


# ------------------------------------------------------------
# 4. ANALYSE INCOME BY SOURCE
# ------------------------------------------------------------

income_by_source = (
    income_df.groupby("Income_Source")["Amount"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values(by="sum", ascending=False)
)

# Rename columns to make the output easier to understand.
income_by_source.columns = [
    "Transaction_Count",
    "Total_Income_KSh",
    "Average_Income_KSh",
    "Median_Income_KSh",
]

print("\nINCOME ANALYSIS BY SOURCE")
print("-" * 60)

print(income_by_source.round(2).to_string())


# ------------------------------------------------------------
# 5. ANALYSE INCOME BY USER
# ------------------------------------------------------------

income_by_user = (
    income_df.groupby("User_ID")["Amount"]
    .agg(["count", "sum", "mean"])
    .sort_values(by="sum", ascending=False)
)

income_by_user.columns = [
    "Income_Transactions",
    "Total_Income_KSh",
    "Average_Income_KSh",
]

print("\nINCOME ANALYSIS BY USER")
print("-" * 60)

print(income_by_user.round(2).to_string())


# ------------------------------------------------------------
# 6. ANALYSE MONTHLY INCOME
# ------------------------------------------------------------

# Create a Year-Month column for grouping transactions.
income_df["Year_Month"] = (
    income_df["Date"].dt.to_period("M")
)

monthly_income = (
    income_df.groupby("Year_Month")["Amount"]
    .sum()
    .sort_index()
)

print("\nMONTHLY INCOME SUMMARY")
print("-" * 60)

print(f"Months with recorded income: {len(monthly_income)}")

print(
    "Average monthly income across the dataset: "
    f"KSh {monthly_income.mean():,.2f}"
)

print(
    "Highest total monthly income: "
    f"KSh {monthly_income.max():,.2f}"
)

print(
    "Lowest total monthly income: "
    f"KSh {monthly_income.min():,.2f}"
)


# ------------------------------------------------------------
# 7. FINAL NOTES
# ------------------------------------------------------------

print("\nANALYSIS NOTES")
print("-" * 60)

print("Dataset: Synthetic financial transactions.")
print("Currency: Kenyan Shillings (KSh).")
print("Income excludes expenses and savings transfers.")
print("Results describe fictional data, not actual Kenyan households.")

print("\nIncome analysis completed successfully.")

