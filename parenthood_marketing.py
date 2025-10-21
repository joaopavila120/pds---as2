import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:
    df = df.copy()
    customers = customers.copy()

    # Merge retail and customer info on CustomerID
    merged = pd.merge(df[["CustomerID", "Country"]], customers[["CustomerID", "NumChildren"]], on="CustomerID", how="inner")

    # Keep one record per customer-country to avoid counting the same customer multiple times
    merged_unique = merged.drop_duplicates(subset=["CustomerID", "Country"])

    # Average number of children per country
    avg_children = merged_unique.groupby("Country")["NumChildren"].mean()

    # Top 5 countries with highest average
    top_5 = avg_children.sort_values(ascending=False).head(5)

    # Return country names as list
    return list(top_5.index)
