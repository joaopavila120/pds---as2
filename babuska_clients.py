import pandas as pd

def babuska_clients(df, customers) -> float:
    df = df.copy()
    customers = customers.copy()

    # Filter only the rows where the product is "HAND WARMER BABUSHKA DESIGN"
    babuska_sales = df[df["Description"] == "HAND WARMER BABUSHKA DESIGN"]

    # Get the unique CustomerIDs who bought this product
    babuska_customers = babuska_sales["CustomerID"].unique()

    # Filter the customers DataFrame to keep only these clients
    babuska_info = customers[customers["CustomerID"].isin(babuska_customers)]

    # Return the average age of these customers
    return babuska_info["Age"].mean()
