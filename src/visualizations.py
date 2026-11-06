# ============================================================
# PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM
# DATA VISUALIZATION
# ============================================================
# Purpose:
# 1. Visualize total income by source.
# 2. Visualize total expenses by category.
# 3. Compare monthly income and expenses over time.
#
# Dataset: Synthetic financial transactions
# Currency: Kenyan Shillings (KSh)
# Period: January 2025 - December 2026
# ============================================================

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


# ============================================================
# 1. PROJECT PATHS AND CONFIGURATION
# ============================================================

# Identify the main project directory.
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Location of the synthetic dataset.
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "synthetic_financial_transactions.csv"
)

# Folder where charts will be saved.
OUTPUT_DIR = PROJECT_DIR / "outputs" / "charts"

# Create the charts folder automatically if it does not exist.
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD AND PREPARE THE DATASET
# ============================================================

df = pd.read_csv(DATA_FILE)

# Convert the Date column into a proper datetime format.
df["Date"] = pd.to_datetime(df["Date"], errors="raise")

# Ensure transaction amounts are numeric.
df["Amount"] = pd.to_numeric(df["Amount"], errors="raise")

# Sort transactions chronologically.
df = df.sort_values("Date").copy()

print("=" * 65)
print("PERSONAL FINANCE AND SPENDING INTELLIGENCE SYSTEM")
print("DATA VISUALIZATION")
print("=" * 65)

print(f"\nDataset loaded successfully: {len(df):,} transactions")
print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Charts will be saved in: {OUTPUT_DIR}")


# ============================================================
# 3. VISUALIZATION ONE: TOTAL INCOME BY SOURCE
# ============================================================

# Income transactions only.
income_df = df[df["Type"] == "Income"].copy()

# Calculate total income received from each source.
income_by_source = (
    income_df.groupby("Income_Source")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Create the chart.
fig, ax = plt.subplots(figsize=(11, 6))

income_by_source.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Total Income by Source",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Income Source", fontsize=11)
ax.set_ylabel("Total Income (KSh)", fontsize=11)

# Display amounts as ordinary numbers with thousands separators.
ax.yaxis.set_major_formatter(
    StrMethodFormatter("{x:,.0f}")
)

# Rotate category labels for readability.
plt.setp(
    ax.get_xticklabels(),
    rotation=35,
    ha="right"
)

ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

fig.tight_layout()

# Save the chart automatically.
income_chart_path = OUTPUT_DIR / "income_by_source.png"

fig.savefig(
    income_chart_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

print("\n1. Income chart created successfully.")
print(f"   Saved to: {income_chart_path}")


# ============================================================
# 4. VISUALIZATION TWO: TOTAL EXPENSES BY CATEGORY
# ============================================================

# Select expense transactions only.
expense_df = df[df["Type"] == "Expense"].copy()

# Calculate total expenses for each category.
expenses_by_category = (
    expense_df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Create a vertical bar chart.
fig, ax = plt.subplots(figsize=(12, 7))

expenses_by_category.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Total Expenses by Category",
    fontsize=15,
    fontweight="bold"
)

# X-axis: Expense categories.
ax.set_xlabel("Expense Category", fontsize=11)

# Y-axis: Total expenses in Kenyan shillings.
ax.set_ylabel("Total Expenses (KSh)", fontsize=11)

# Format amounts with thousands separators.
ax.yaxis.set_major_formatter(
    StrMethodFormatter("{x:,.0f}")
)

# Rotate category labels so they are easier to read.
plt.setp(
    ax.get_xticklabels(),
    rotation=35,
    ha="right"
)

ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

fig.tight_layout()

# Save the chart automatically.
expense_chart_path = OUTPUT_DIR / "expenses_by_category.png"

fig.savefig(
    expense_chart_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("\n2. Expense chart created successfully.")
print(f"   Saved to: {expense_chart_path}")

# ============================================================
# 5. VISUALIZATION THREE: MONTHLY INCOME VS. EXPENSES
# ============================================================

# Calculate monthly income.
monthly_income = (
    income_df
    .set_index("Date")["Amount"]
    .resample("MS")
    .sum()
)

# Calculate monthly expenses.
monthly_expenses = (
    expense_df
    .set_index("Date")["Amount"]
    .resample("MS")
    .sum()
)

# Combine monthly income and expenses into one table.
monthly_financial_summary = pd.concat(
    [
        monthly_income.rename("Income"),
        monthly_expenses.rename("Expenses")
    ],
    axis=1
).fillna(0)

# Ensure months are displayed in chronological order.
monthly_financial_summary = monthly_financial_summary.sort_index()

# Create the chart.
fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(
    monthly_financial_summary.index,
    monthly_financial_summary["Income"],
    marker="o",
    linewidth=2,
    label="Income"
)

ax.plot(
    monthly_financial_summary.index,
    monthly_financial_summary["Expenses"],
    marker="o",
    linewidth=2,
    label="Expenses"
)

ax.set_title(
    "Monthly Income vs. Expenses",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Amount (KSh)", fontsize=11)

# Format amounts with thousands separators.
ax.yaxis.set_major_formatter(
    StrMethodFormatter("{x:,.0f}")
)

# Display readable month labels.
fig.autofmt_xdate(rotation=45)

ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

fig.tight_layout()

# Save the chart automatically.
monthly_chart_path = OUTPUT_DIR / "monthly_income_vs_expenses.png"

fig.savefig(
    monthly_chart_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

print("\n3. Monthly income-versus-expenses chart created successfully.")
print(f"   Saved to: {monthly_chart_path}")


# ============================================================
# 6. MONTHLY FINANCIAL SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("MONTHLY FINANCIAL SUMMARY")
print("=" * 65)

print(
    monthly_financial_summary.to_string(
        formatters={
            "Income": lambda value: f"KSh {value:,.2f}",
            "Expenses": lambda value: f"KSh {value:,.2f}"
        }
    )
)

print("\n" + "=" * 65)
print("VISUALIZATION PROCESS COMPLETED SUCCESSFULLY")
print("=" * 65)

print("\nCharts created:")
print("1. income_by_source.png")
print("2. expenses_by_category.png")
print("3. monthly_income_vs_expenses.png")

print(f"\nOutput directory: {OUTPUT_DIR}")

print(
    "\nNote: These visualizations use synthetic data and do not "
    "represent actual financial records or spending patterns "
    "of Kenyan households."
)