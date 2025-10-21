import pandas as pd

def amount_spent_computer(df) -> pd.DataFrame:
    
    df = df.copy()
    
    df["amount_spent"] = df["Quantity"] * df["UnitPrice"]
    
    return df
