import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    df = df.copy()
    customers = customers.copy()

    # Get the list of the top 5 customers
    top_customers = top_five_cust(df)

    # Filter the customer DataFrame to keep only those 5
    top_customers_info = customers[customers["CustomerID"].isin(top_customers)]

    # Calculate and return the average age of these top 5 customers
    return top_customers_info["Age"].mean()
