import pandas as pd

def top_five_spenders(df) -> list:
    total_spent = df.groupby('CustomerID')['amount_spent'].sum()

    top_spenders = total_spent.sort_values(ascending=False).head(5)

    return top_spenders.index.tolist()
