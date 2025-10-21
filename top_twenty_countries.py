import pandas as pd
from typing import List

def top_twenty_countries(df) -> List[str]:
    
    df = df.copy()

    # Remove duplicate orders based on InvoiceNo
    unique_orders = df.drop_duplicates(subset=["InvoiceNo"])

    # Count unique orders per country and take the top 20
    top_20 = unique_orders["Country"].value_counts().head(20)

    # Return the country names as a list
    return list(top_20.index)
