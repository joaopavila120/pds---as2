import pandas as pd
from typing import List

def popular_products(df) -> List[str]:

    df = df.copy()

    product_counts = df["Description"].value_counts()

    top5 = product_counts.head(5).index.tolist()

    return top5
