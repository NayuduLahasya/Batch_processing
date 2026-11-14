import pandas as pd

transactions = pd.read_csv(
    "output/deduplicated_transactions.csv"
)

accounts = pd.read_csv(
    "data/accounts.csv"
)

transactions["status"] = transactions["account_id"].apply(
    lambda x: "VALID"
    if x in accounts["account_id"].values
    else "INVALID"
)

valid_df = transactions[
    transactions["status"] == "VALID"
]

invalid_df = transactions[
    transactions["status"] == "INVALID"
]

valid_df.to_csv(
    "output/validated_transactions.csv",
    index=False
)

invalid_df.to_csv(
    "output/invalid_accounts.csv",
    index=False
)

print("Validation completed")