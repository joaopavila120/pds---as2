import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    
    df = df.copy()
    
    # Drop rows where 'CustomerID' OR 'Description' has a missing value
    df = df.dropna(subset=["CustomerID", "Description"])
    
    return df
