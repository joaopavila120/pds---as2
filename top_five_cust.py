import pandas as pd

def top_five_cust(df) -> list:
    
    order_counts = df.groupby('CustomerID')['InvoiceNo'].nunique()

    top_customers = order_counts.sort_values(ascending=False).head(5)
    
    return top_customers.index.tolist()
