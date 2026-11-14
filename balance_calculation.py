import pandas as pd

df = pd.read_csv(
    "output/validated_transactions.csv"
)

df["net_amount"] = df.apply(
    lambda x:
    x["amount"]
    if x["txn_type"] == "CREDIT"
    else -x["amount"],
    axis=1
)

balances = (
    df.groupby("account_id")["net_amount"]
      .sum()
      .reset_index()
)

balances = balances.rename(
    columns={"net_amount": "balance"}
)

balances.to_csv(
    "output/balances.csv",
    index=False
)

print("Balance calculation completed")