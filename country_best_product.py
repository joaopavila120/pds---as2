import pandas as pd

def country_best_product(df, country) -> str:

    df = df.copy()

    if country not in df["Country"].unique():
        return None

    country_df = df[df["Country"] == country]

    product_counts = country_df["Description"].value_counts()

    most_popular = product_counts.idxmax()

    return most_popular

