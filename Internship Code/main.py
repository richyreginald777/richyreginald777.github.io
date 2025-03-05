import pandas as pd

df = pd.read_csv('/Users/richyreginald/Desktop/sales.csv')

df["Item"] = df['Item'].fillna("null")
df['Quantity'] = df['Quantity'].fillna(0)

print()
