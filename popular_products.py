import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    
    df = df.copy()

    # Count the occurrences of each product description
    product_counts = df["Description"].value_counts()

    # Select the top 5 most purchased products
    top_5 = product_counts.head(5)

    # Return only the product names as a list
    return list(top_5.index)
