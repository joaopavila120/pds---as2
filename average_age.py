import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:

    top5_ids = top_five_cust(df)

    top5_customers = customers[customers["CustomerID"].isin(top5_ids)]

    avg_age = top5_customers["Age"].mean()

    return float(avg_age)
