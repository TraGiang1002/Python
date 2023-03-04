import pandas as pd
import numpy as np

df = pd.read_csv("chipotle.tsv", sep="\t")
print(df.head(5))
print(df.shape)
print(df.info())
print(df.columns)
print(df.index)
print(df.describe())
print(df.describe(include="all"))
print(df)
print(df.loc[(df.quantity == 2) & (df.item_name == "Nantucket Nectar"), ['order_id', 'quantity', 'item_name']])
print(df.iloc[9])
print(df.iloc[[9]])
print(df.iloc[3:5, :-1])

print(df.item_price.dtype)
df.item_price = df.item_price.apply(lambda x: float(x.replace('$', '')))
print(df)
df["total_price"] = df["quantity"]*df["item_price"]
print(df)
print(df.total_price.sum())
c = df.groupby("item_name")["quantity"].sum()
print(c)
print(c.sort_values(ascending=False).head(5))
print(df.item_name.value_counts().count())
print(df.item_name.nunique())