import pandas as pd

df = pd.read_csv("data/transactions.csv")

df = df.drop_duplicates(subset=["transaction_id"])

df.to_csv("output/deduplicated_transactions.csv", index=False)

print("Duplicates removed")