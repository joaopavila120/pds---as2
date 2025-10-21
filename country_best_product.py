import pandas as pd

def country_best_product(df, country) -> str:
    df = df.copy()
    
    # Only the rows from the country passed as an argument
    sub = df[df["Country"] == country]
    
    # Check if the country exists in the data
    if sub.empty:
        return None
    
    # Count how many times each product appears (not quantity)
    counts = sub["Description"].value_counts()
    
    return counts.index[0]
