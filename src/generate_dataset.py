"""
Personal Finance and Spending Intelligence System
Synthetic Financial Dataset Generator

Creates 3,000 fictional transactions for 10 users between
January 2025 and December 2026.

Currency: Kenyan Shillings (KES).

All data is fictional and intended for educational and
portfolio demonstration purposes.
"""

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd


# ============================================================
# 1. REPRODUCIBILITY AND FILE PATHS
# ============================================================

random.seed(42)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "synthetic_financial_transactions.csv"
)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. DATASET SETTINGS
# ============================================================

TOTAL_TRANSACTIONS = 3000

START_DATE = date(2025, 1, 1)
END_DATE = date(2026, 12, 31)

PAYMENT_METHODS = [
    "M-Pesa",
    "Cash",
    "Bank Transfer",
    "Debit Card"
]


# ============================================================
# 3. FICTIONAL USER PROFILES
# ============================================================

USERS = {
    "USER001": {
        "profile": "Salaried Employee",
        "monthly_salary": 65000,
        "income_sources": ["Employment"],
        "income_weights": [100],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [25, 15, 15, 12, 10, 6, 7, 10]
    },

    "USER002": {
        "profile": "Salaried Employee",
        "monthly_salary": 85000,
        "income_sources": ["Employment"],
        "income_weights": [100],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [20, 20, 12, 12, 12, 7, 7, 10]
    },

    "USER003": {
        "profile": "Small Business Owner",
        "monthly_salary": None,
        "income_sources": [
            "Business", "Investment Returns", "Gifts"
        ],
        "income_weights": [85, 10, 5],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [20, 15, 15, 12, 10, 8, 5, 15]
    },

    "USER004": {
        "profile": "Freelancer",
        "monthly_salary": None,
        "income_sources": [
            "Freelancing", "Gifts", "Investment Returns"
        ],
        "income_weights": [85, 10, 5],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [20, 18, 12, 10, 10, 8, 7, 15]
    },

    "USER005": {
        "profile": "Student",
        "monthly_salary": None,
        "income_sources": [
            "Family Support", "Casual Work", "Tutoring", "Gifts"
        ],
        "income_weights": [65, 15, 15, 5],
        "expense_categories": [
            "Food", "Transport", "School Fees", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [25, 18, 18, 5, 10, 7, 10, 7]
    },

    "USER006": {
        "profile": "Casual Worker",
        "monthly_salary": None,
        "income_sources": ["Casual Work", "Gifts"],
        "income_weights": [95, 5],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [25, 18, 18, 10, 8, 8, 3, 12]
    },

    "USER007": {
        "profile": "Salaried Employee",
        "monthly_salary": 45000,
        "income_sources": ["Employment"],
        "income_weights": [100],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [25, 20, 15, 10, 8, 7, 5, 10]
    },

    "USER008": {
        "profile": "Small Business Owner",
        "monthly_salary": None,
        "income_sources": [
            "Business", "Gifts", "Investment Returns"
        ],
        "income_weights": [85, 10, 5],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [20, 15, 15, 12, 10, 8, 5, 15]
    },

    "USER009": {
        "profile": "Freelancer",
        "monthly_salary": None,
        "income_sources": [
            "Freelancing", "Tutoring", "Gifts"
        ],
        "income_weights": [75, 20, 5],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [20, 18, 12, 10, 10, 8, 7, 15]
    },

    "USER010": {
        "profile": "Household Manager",
        "monthly_salary": None,
        "income_sources": [
            "Family Support", "Business", "Gifts"
        ],
        "income_weights": [75, 15, 10],
        "expense_categories": [
            "Food", "Rent", "Transport", "Utilities",
            "Shopping", "Health", "Entertainment", "Other Expenses"
        ],
        "expense_weights": [30, 15, 10, 15, 12, 8, 3, 7]
    }
}


# ============================================================
# 4. EXPENSE AMOUNT RANGES (KES)
# ============================================================

EXPENSE_RANGES = {
    "Food": (100, 8000),
    "Rent": (5000, 35000),
    "Transport": (50, 6000),
    "School Fees": (1000, 60000),
    "Utilities": (200, 8000),
    "Shopping": (200, 15000),
    "Health": (200, 12000),
    "Entertainment": (100, 6000),
    "Other Expenses": (100, 10000)
}


# ============================================================
# 5. INCOME CATEGORY MAPPING
# ============================================================

INCOME_CATEGORY_MAP = {
    "Employment": "Employment Income",
    "Business": "Business Income",
    "Freelancing": "Freelance Income",
    "Casual Work": "Casual Work Income",
    "Tutoring": "Tutoring Income",
    "Family Support": "Family Support",
    "Gifts": "Gifts",
    "Investment Returns": "Investment Returns"
}


INCOME_RANGES = {
    "Employment": (25000, 120000),
    "Business": (2000, 50000),
    "Freelancing": (1500, 40000),
    "Casual Work": (500, 8000),
    "Tutoring": (500, 10000),
    "Family Support": (1000, 25000),
    "Gifts": (500, 15000),
    "Investment Returns": (500, 10000)
}


# ============================================================
# 6. TRANSACTION DESCRIPTIONS
# ============================================================

EXPENSE_DESCRIPTIONS = {
    "Food": [
        "Groceries", "Market shopping",
        "Restaurant meal", "Food delivery"
    ],
    "Rent": [
        "Monthly rent", "House rent payment"
    ],
    "Transport": [
        "Matatu fare", "Fuel purchase",
        "Taxi fare", "Motorcycle transport"
    ],
    "School Fees": [
        "School fees payment", "College fees",
        "School supplies"
    ],
    "Utilities": [
        "Electricity tokens", "Water bill",
        "Internet bill", "Gas refill"
    ],
    "Shopping": [
        "Clothing purchase", "Household shopping",
        "Personal items"
    ],
    "Health": [
        "Pharmacy purchase", "Medical consultation",
        "Health insurance payment"
    ],
    "Entertainment": [
        "Movie tickets", "Entertainment subscription",
        "Social outing"
    ],
    "Other Expenses": [
        "Miscellaneous expense", "Personal expense",
        "Unexpected expense"
    ]
}


INCOME_DESCRIPTIONS = {
    "Business": [
        "Business sales",
        "Business payment received",
        "Customer payment"
    ],
    "Freelancing": [
        "Freelance project payment",
        "Consulting payment",
        "Online work payment"
    ],
    "Casual Work": [
        "Casual work wages",
        "Temporary work payment"
    ],
    "Tutoring": [
        "Tutoring payment",
        "Private lesson payment"
    ],
    "Family Support": [
        "Family support received",
        "Household support received"
    ],
    "Gifts": [
        "Gift received",
        "Personal support received"
    ],
    "Investment Returns": [
        "Investment return",
        "Investment payment received"
    ]
}


# ============================================================
# 7. HELPER FUNCTIONS
# ============================================================

def random_date_in_month(year, month):
    """Generate a random valid date in a specified month."""

    first_day = date(year, month, 1)

    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)

    last_day = next_month - timedelta(days=1)

    return first_day + timedelta(
        days=random.randint(0, (last_day - first_day).days)
    )


def generate_income(profile):
    """Generate income based on a user's profile."""

    source = random.choices(
        profile["income_sources"],
        weights=profile["income_weights"],
        k=1
    )[0]

    if source == "Employment":
        amount = profile["monthly_salary"] * random.uniform(0.97, 1.03)
        description = "Monthly salary"
    else:
        minimum, maximum = INCOME_RANGES[source]
        amount = random.uniform(minimum, maximum)
        description = random.choice(INCOME_DESCRIPTIONS[source])

    category = INCOME_CATEGORY_MAP[source]

    return round(amount, 2), source, category, description


def generate_expense(profile):
    """Generate an expense using the user's profile."""

    category = random.choices(
        profile["expense_categories"],
        weights=profile["expense_weights"],
        k=1
    )[0]

    minimum, maximum = EXPENSE_RANGES[category]
    amount = random.uniform(minimum, maximum)

    # Use a lower rent range for the fictional student.
    if profile["profile"] == "Student" and category == "Rent":
        amount = random.uniform(1000, 10000)

    description = random.choice(EXPENSE_DESCRIPTIONS[category])

    return round(amount, 2), category, description


def create_transaction(
    user_id,
    transaction_date,
    description,
    category,
    income_source,
    amount,
    transaction_type,
    payment_method
):
    """Create one standardized transaction record."""

    return {
        "User_ID": user_id,
        "Date": transaction_date,
        "Description": description,
        "Category": category,
        "Income_Source": income_source,
        "Amount": amount,
        "Type": transaction_type,
        "Payment_Method": payment_method
    }


# ============================================================
# 8. GENERATE REGULAR SALARY TRANSACTIONS
# ============================================================

transactions = []

for user_id, profile in USERS.items():

    if profile["profile"] == "Salaried Employee":

        for year in (2025, 2026):
            for month in range(1, 13):

                salary_date = date(year, month, 25)

                if START_DATE <= salary_date <= END_DATE:

                    amount, source, category, description = (
                        generate_income(profile)
                    )

                    transactions.append(
                        create_transaction(
                            user_id=user_id,
                            transaction_date=salary_date,
                            description=description,
                            category=category,
                            income_source=source,
                            amount=amount,
                            transaction_type="Income",
                            payment_method="Bank Transfer"
                        )
                    )


# ============================================================
# 9. GENERATE ADDITIONAL TRANSACTIONS
# ============================================================

# Generate enough candidates to select 3,000 transactions while
# retaining every scheduled salary transaction.

while len(transactions) < TOTAL_TRANSACTIONS * 2:

    user_id = random.choice(list(USERS.keys()))
    profile = USERS[user_id]

    transaction_type = random.choices(
        ["Income", "Expense", "Transfer"],
        weights=[25, 65, 10],
        k=1
    )[0]

    transaction_date = START_DATE + timedelta(
        days=random.randint(0, (END_DATE - START_DATE).days)
    )

    payment_method = random.choice(PAYMENT_METHODS)

    if transaction_type == "Income":

        amount, source, category, description = generate_income(profile)

        # Salaries are already scheduled monthly above.
        if source == "Employment":
            continue

    elif transaction_type == "Expense":

        amount, category, description = generate_expense(profile)
        source = "Not applicable"

    else:

        amount = round(random.uniform(500, 20000), 2)
        category = "Savings Transfers"
        description = "Transfer to savings"
        source = "Not applicable"

        payment_method = random.choice([
            "M-Pesa",
            "Bank Transfer"
        ])

    transactions.append(
        create_transaction(
            user_id=user_id,
            transaction_date=transaction_date,
            description=description,
            category=category,
            income_source=source,
            amount=amount,
            transaction_type=transaction_type,
            payment_method=payment_method
        )
    )


# ============================================================
# 10. SELECT EXACTLY 3,000 TRANSACTIONS
# ============================================================

salary_transactions = [
    row for row in transactions
    if row["Category"] == "Employment Income"
]

other_transactions = [
    row for row in transactions
    if row["Category"] != "Employment Income"
]

remaining_count = TOTAL_TRANSACTIONS - len(salary_transactions)

selected_transactions = (
    salary_transactions
    + random.sample(other_transactions, remaining_count)
)


# ============================================================
# 11. CREATE AND FORMAT THE DATAFRAME
# ============================================================

df = pd.DataFrame(selected_transactions)

df = df.sort_values(
    by=["Date", "User_ID"]
).reset_index(drop=True)

df.insert(
    0,
    "Transaction_ID",
    [f"TXN{i:05d}" for i in range(1, len(df) + 1)]
)

df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
df["Amount"] = df["Amount"].round(2)


# ============================================================
# 12. SAVE THE DATASET
# ============================================================

df.to_csv(OUTPUT_FILE, index=False)


# ============================================================
# 13. GENERATION SUMMARY
# ============================================================

print("=" * 60)
print("SYNTHETIC FINANCIAL DATASET GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Output file: {OUTPUT_FILE}")
print(f"Number of transactions: {len(df)}")
print(f"Number of fictional users: {df['User_ID'].nunique()}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

print("\nTransaction counts:")
print(df["Type"].value_counts())

print("\nCategory counts:")
print(df["Category"].value_counts())

print("\nIncome sources:")
print(
    df.loc[df["Type"] == "Income", "Income_Source"].value_counts()
)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nFirst five records:")
print(df.head())

print("\nAll data is fictional and denominated in KES.")
print("=" * 60)

