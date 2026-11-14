import pandas as pd

# Read source files
transactions = pd.read_csv(
    "data/transactions.csv"
)

accounts = pd.read_csv(
    "data/accounts.csv"
)

# Valid account list
valid_accounts = set(
    accounts["account_id"]
)

# Invalid Accounts
invalid_accounts = transactions[
    ~transactions["account_id"].isin(valid_accounts)
].copy()

# Valid Accounts Transactions
valid_transactions = transactions[
    transactions["account_id"].isin(valid_accounts)
].copy()

# Invalid Transactions
invalid_transactions = valid_transactions[
    valid_transactions["amount"] > 100000
].copy()

# Save separately
invalid_accounts.to_csv(
    "output/invalid_accounts.csv",
    index=False
)

invalid_transactions.to_csv(
    "output/invalid_transactions.csv",
    index=False
)

# Create combined anomaly report
invalid_accounts["issue_type"] = "INVALID_ACCOUNT"
invalid_transactions["issue_type"] = "INVALID_TRANSACTION"

anomaly_report = pd.concat(
    [invalid_accounts, invalid_transactions],
    ignore_index=True
)

anomaly_report.to_csv(
    "output/anomaly_report.csv",
    index=False
)

print("Anomaly report generated")
