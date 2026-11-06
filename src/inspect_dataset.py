"""
Personal Finance and Spending Intelligence System
-------------------------------------------------
Purpose:
Perform initial data-quality checks on the synthetic dataset.
"""

from pathlib import Path

import pandas as pd


# ============================================================
# 1. LOAD THE SYNTHETIC DATASET
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "synthetic_financial_transactions.csv"
)

df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("INITIAL DATASET INSPECTION")
print("=" * 60)


# ============================================================
# 2. INSPECT DATASET DIMENSIONS AND STRUCTURE
# ============================================================

print("\n1. DATASET DIMENSIONS")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n2. COLUMN NAMES")
print(df.columns.tolist())

print("\n3. DATA TYPES")
print(df.dtypes)

print("\n4. FIRST FIVE ROWS")
print(df.head())


# ============================================================
# 3. CHECK MISSING VALUES
# ============================================================

print("\n5. MISSING VALUES PER COLUMN")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())


# ============================================================
# 4. CHECK DUPLICATE RECORDS
# ============================================================

print("\n6. DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n7. DUPLICATE TRANSACTION IDS")
print(df["Transaction_ID"].duplicated().sum())


# ============================================================
# 5. CHECK UNIQUE USERS AND TRANSACTION TYPES
# ============================================================

print("\n8. NUMBER OF UNIQUE USERS")
print(df["User_ID"].nunique())

print("\n9. TRANSACTION TYPES")
print(df["Type"].value_counts())

print("\n10. TRANSACTION CATEGORIES")
print(df["Category"].value_counts())


# ============================================================
# 6. CHECK AMOUNT VALUES
# ============================================================

print("\n11. AMOUNT SUMMARY")
print(df["Amount"].describe())

print("\n12. ZERO OR NEGATIVE AMOUNTS")
print((df["Amount"] <= 0).sum())


# ============================================================
# 7. CHECK TRANSACTION TYPE AND CATEGORY CONSISTENCY
# ============================================================

print("\n13. CATEGORY AND TYPE COMBINATIONS")
print(
    pd.crosstab(
        df["Category"],
        df["Type"]
    )
)


# ============================================================
# 8. CHECK INCOME SOURCE CONSISTENCY
# ============================================================

print("\n14. INCOME SOURCE BY TRANSACTION TYPE")
print(
    pd.crosstab(
        df["Income_Source"].fillna("Not applicable"),
        df["Type"]
    )
)


# ============================================================
# 9. CHECK DATE RANGE
# ============================================================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

print("\n15. INVALID DATES")
print(df["Date"].isna().sum())

print("\n16. DATE RANGE")
print("Earliest:", df["Date"].min())
print("Latest:", df["Date"].max())


# ============================================================
# 10. CHECK TRANSACTION ID UNIQUENESS
# ============================================================

print("\n17. UNIQUE TRANSACTION IDS")
print(df["Transaction_ID"].nunique())

print("\nInspection completed.")

# ============================================================
# 18. CHECK MONTHLY SALARY CONSISTENCY
# ============================================================

print("\n18. MONTHLY SALARY CONSISTENCY")
print("=" * 60)

# Select transactions classified as salary.
salary_df = df[df["Category"] == "Employment Income"].copy()

# Convert Date to datetime for reliable date analysis.
salary_df["Date"] = pd.to_datetime(salary_df["Date"])

# Extract the year and month of each salary transaction.
salary_df["Year_Month"] = salary_df["Date"].dt.to_period("M")

# Count salary transactions for each user in each month.
salary_counts = salary_df.groupby(
    ["User_ID", "Year_Month"]
).size().unstack(fill_value=0)

print("\nSalary transactions per user per month:")
print(salary_counts)

# Check whether each salaried user has 24 salary transactions.
print("\nTotal salary transactions per user:")
print(salary_df.groupby("User_ID").size())

# Identify months with missing or multiple salary transactions.
print("\nUsers and months with missing or duplicate salary entries:")

issues = salary_counts[
    (salary_counts != 1).any(axis=1)
]

if issues.empty:
    print("No issues found. Every salaried user has one salary each month.")
else:
    print(issues)

# ============================================================
# 19. CHECK TRANSACTION AMOUNT OUTLIERS
# ============================================================

print("\n19. TRANSACTION AMOUNT OUTLIERS")
print("=" * 60)

# Calculate outlier boundaries separately for each category.
outlier_results = []

for category, group in df.groupby("Category"):

    # Calculate the first and third quartiles.
    q1 = group["Amount"].quantile(0.25)
    q3 = group["Amount"].quantile(0.75)

    # Calculate the interquartile range.
    iqr = q3 - q1

    # Calculate the lower and upper outlier boundaries.
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Identify potential outliers.
    outliers = group[
        (group["Amount"] < lower_bound)
        | (group["Amount"] > upper_bound)
    ]

    # Save the results.
    outlier_results.append({
        "Category": category,
        "Q1": round(q1, 2),
        "Q3": round(q3, 2),
        "IQR": round(iqr, 2),
        "Lower_Bound": round(lower_bound, 2),
        "Upper_Bound": round(upper_bound, 2),
        "Outlier_Count": len(outliers)
    })

# Display a summary of potential outliers.
outlier_summary = pd.DataFrame(outlier_results)

print("\nOutlier summary by category:")
print(outlier_summary.to_string(index=False))

# Display a few individual potential outliers for inspection.
print("\nSample potential outlier transactions:")

for category, group in df.groupby("Category"):

    q1 = group["Amount"].quantile(0.25)
    q3 = group["Amount"].quantile(0.75)
    iqr = q3 - q1

    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr

    outliers = group[
        (group["Amount"] < lower_bound)
        | (group["Amount"] > upper_bound)
    ]

    if not outliers.empty:
        print(f"\nCategory: {category}")
        print(
            outliers[
                [
                    "Transaction_ID",
                    "User_ID",
                    "Category",
                    "Amount",
                    "Type"
                ]
            ].head(5).to_string(index=False)
        )

# ============================================================
# 20. INVESTIGATING THE OTHER EXPENSES CATEGORY
# ============================================================

print("\n20. INVESTIGATING THE OTHER EXPENSES CATEGORY")
print("=" * 60)

# Filter transactions belonging to the Other Expenses category
other_expenses_df = df[
    df["Category"] == "Other Expenses"
].copy()

# Check whether any transactions exist in this category
if other_expenses_df.empty:
    print("No transactions found in the Other Expenses category.")

else:
    # Transaction counts by type
    print("\nTransaction counts by type:")
    print(other_expenses_df["Type"].value_counts())

    # Income source counts
    print("\nIncome source counts:")
    print(other_expenses_df["Income_Source"].value_counts())

    # Transaction amount summary
    print("\nTransaction amount summary:")
    print(
        other_expenses_df["Amount"].describe().round(2)
    )

    # Transaction descriptions by type
    print("\nTransaction descriptions by type:")
    print(
        other_expenses_df.groupby("Type")["Description"]
        .value_counts()
    )

    # Display a sample of transactions for manual review
    print("\nSample Other Expenses transactions:")
    print(
        other_expenses_df[
            ["Date", "User_ID", "Description", "Amount", "Type"]
        ].head(10).to_string(index=False)
    )

