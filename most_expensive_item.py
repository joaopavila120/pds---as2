import pandas as pd

def most_expensive_item(df) -> str:
    df = df.copy()
    
    # Find the row with the maximum UnitPrice
    max_price_row = df.loc[df["UnitPrice"].idxmax()]
    
    # Return the description 
    return max_price_row["Description"]
