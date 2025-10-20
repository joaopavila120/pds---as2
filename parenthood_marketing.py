import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:

    merged = pd.merge(df, customers, on="CustomerID", how="inner")

    avg_children_by_country = (
        merged.groupby("Country")["NumChildren"]
        .mean()
        .sort_values(ascending=False)
    )

    top5_countries = avg_children_by_country.head(5).index.tolist()

    return top5_countries

